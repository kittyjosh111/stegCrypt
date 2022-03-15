## stegCrypt
OTP and steganography.

The iOS shortcut equivalent for this script may be found on routinehub [https://].

## Usage
This script relies on numpy and stepic as dependencies. Install it first with ```pip3 install numpy``` and ```pip3 install stepic```. Alternatively, just run ```pip3 install -r requirements.txt``` Then download the script. To execute the script, run ```python3 script.py``` in a terminal. Follow the prompts given. If you want to pass in a text file to encrypt, use the ```-i``` flag. To pass in image files for steganography, ```-e``` will input an image for encryption, or inputs the encrypted message for decryption, and ```-k``` will input the image with the key for decryption. More details below.

## Flags
```-i```: pass in a text file to encrypt. This will automatically choose the encryption process.

```-e```: pass in an image file. For the encryption process, this is the image that will hold the encrypted message. For the decryption process, this is the option to specify which image has the message.

```-k```: pass in key image file. This option is only used during decryption, and passes in the file that has the key string hidden in it.

## About
This script is meant to provide a sort of encryption for simple messages. Say you want to send someone a text message without someone else being able to read it. You can use this shortcut to send a string of numbers containing the message.

This shortcut was based off of the concept of OTP (One Time Pad), so each letter of message is randomly altered; this shortcut uses addition. As I have not extensively studied encryption methods, I could be completely wrong about OTP. The shortcut seems to work anyway.

The script features two processes: an encryption (0) and decryption (1).

The encrypted message and key are then hidden in an image file using stepic, a python module that performs steganography. The image containing the encrypted message looks like the inputted image, whereas the image containing the key looks reversed.

The TLDR of the mechanism:

- Split message into letters, spaces, basic punctuation

- Assign numeric value to each split item (ASCII)

- Randomly generate number as key

- Add said random key to aforementioned number

- Export final message and key to image files

## Example
For example, let's encrypt the string ```hello```. 
We will also pass in the image file ```python.png``` using the flag like this: ```-e python.png```.

To encrypt, select option ```0``` when starting the script. The script will split each letter of the string apart, creating a list of 

```
h
e
l
l
o
```

Each character is then converted to ASCII, which becomes 

```
104
101
105
105
111
```

For each number, a random "key" is generated, which is a random integer from 2 to 750, wihch is then added to the number in the ASCII list. If for example our keys were generated as 

```
1
2
1
3
4
```

then our final encrypted message is:

```
104 + 1 = 105
101 + 2 = 103
105 + 1 = 106
105 + 3 = 108
111 + 4 = 115
```

Then the encrypted message and the key are combined with colons and exported.

```
encrypted message = 105:103:106:108:115
final key = 1:2:1:3:4
```
The encrypted message is then hidden in a new image which should be visually similar to the original ```python.png```. This file is renamed to ```encryptedMessage.png```.

The key is exported into an image file that is the visual reverse of the file, saved as ```key.png```.

To decrypt, run the script with ```-e encryptedMessage.png -k key.png```. Adjust the file names if you renamed the images.

The decrypt process will get the encrypted message and key from the image files, then run the encryption process in reverse.

```
105 - 1 = 104 = h
103 - 2 = 101 = e
106 - 1 = 105 = l
108 - 3 = 105 = l
115 - 4 = 111 = o
```
