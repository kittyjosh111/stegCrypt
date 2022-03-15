## encryption 

~/stegCrypt$ ls

```python.png  README.md  requirements.txt  script.py```

~/stegCrypt$ python3 script.py -e python.png 

```Choose an option: [0]=Encrypt Message, [1]=Decrypt Message```

```0```

```Input the message you want to encrypt:```

```hello```

~/stegCrypt$ 

## decryption

~/stegCrypt$ ls

```encryptedMessage.png key.png README.md script.py example.md python.png requirements.txt```

~/stegCrypt$ python3 script.py -e encryptedMessage.png -k key.png 

```Choose an option: [0]=Encrypt Message, [1]=Decrypt Message```

```1```

```- Your decrypted message is below -```

```hello```

~/stegCrypt$ 