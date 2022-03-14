#python 3.x
#Crypt with extra steps. Meant to be two separate projects, this is with steganography.
#from select import select -VSC wanted to add this in, idk why.

from PIL import Image
from numpy import char
import stepic
import argparse
import random

#variables
text = ""
selectPhoto = ""
encodePhoto = ""

#parser to input text file
parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='input', help='Pass in plaintext file to encrypt')
parser.add_argument('-e', dest='photoE', help='Pass in image file for encrypted message')
parser.add_argument('-k', dest='photoK', help='Pass in image file for key')
args = parser.parse_args()

#define encryption method
def encryption(providedInput):

    #variables
    encrypt = ""
    encode = "" 
    key = ""
    finalKey = ""

    for character in providedInput:
        #generates random number to addd to the string converted to ASCII
        key = random.randint(2,750)
        encrypt = int(key) + int((ord(character))) #ord allows for string to ASCII
        encode = str(encode) + str(encrypt) + ":"
        finalKey = str(finalKey) + str(key) + ":"

    key = finalKey[:-1] #removes the final colon
    keyByte = key.encode('utf-8') #convert key to byte for use with stepic
    encode = encode[:-1] #removes the final colon
    encodeByte = encode.encode('utf-8') #convert encode to byte for use with stepic

    #steganography portion. Saves encrypted message (E) and key (K) to different images specified.
    selectPhotoE = Image.open(args.photoE)
    selectPhotoK = Image.open(args.photoK)
    encodePhotoE = stepic.encode(selectPhotoE, encodeByte)
    encodePhotoE.save('encryptedMessage.png', 'PNG') 
    encodePhotoK = stepic.encode(selectPhotoK, keyByte)
    encodePhotoK.save('key.png', 'PNG') 

#define what to do without passing in file input
def function():
    #choose to encrypt or decrypt
    chooseFromMenu = int(input("Choose an option: [0]=Encrypt Message, [1]=Decrypt Message\n"))

    #choose from menu when no file passed
    if chooseFromMenu == 0:
        providedInput = input("Input the message you want to encrypt:\n")   
        encryption(providedInput)
        
    else:
        #variables
        d = ""
        decoded = ""
        decrypted=""
        key = ""
        splitText = ""
        splitKey = ""

        #decryption and give error
        try:
            
            #get text from images (E is encoded, K is key)
            selectPhotoE = Image.open(args.photoE)
            providedInput = stepic.decode(selectPhotoE)
            selectPhotoK = Image.open(args.photoK)
            key = stepic.decode(selectPhotoK)

            splitText = providedInput.split(":")
            splitKey = key.split(":")
            i = 0

            #loops through for each item in split, analogous to 'repeat with each'
            while i < len(splitText):
                d = int(splitText[i]) - int(splitKey[i])
                decoded = chr(int(d)) #chr allows for ASCII to string
                decrypted = str(decrypted) + str(decoded)
                i += 1
            
            print("\n- Your decrypted message is below -\n" + decrypted + "\n")

        except: #give error when there is an error
            print("\nError. Check your image and encrypted message.\n")

#main function
try:
    #reading said text file
    file = open(args.input)
    while True:
        nextLine = file.readline()

        if not nextLine:
            break;
        text = str(text) + str(nextLine.strip()) + "\n" 

    file.close()
    providedInput = text
    encryption(providedInput)

except:
    function()