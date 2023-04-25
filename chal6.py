#!bin/usr/python3

#Code Challenge 6
#Stanley L. Ferguson III
#24 Apr 223
#create a script that uses cryptography library to encrypt and decrypt files and messages

#import libraries
from cryptography.fernet import Fernet 

#create the key and save to file
def forge_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#load key from key.key
def getkey():
    return open("key.key", "rb").read()

#make the ugandan key
forge_key()

#load the ugandan key
key = getkey()

#assign message variable
message = "follow me, I know de way".encode

#assign encryption variable
encryption = Fernet(key)

#assign an encryption for message and file
encryptedmsg = encryption.encrypt(message)
encryptedfile = encryption.encrypt(deway.txt) 

#assign decryption for message and files
decryptmsg = encryption.decrypt(message)
decryptfile = encryption.decrypt(deway.txt)

#encrypt a file
def hide_dekey():
    encryptedfile
    print("I swallow de key")

#decrypt a file
def find_dekey():
    decryptfile
    print(deway.txt)
#encrypt a message
def hide_deway():
    encryptedmsg
    print("dey do not know de way")
    
#decrpyt a message
def show_deway():
    decryptmsg
    print("now you can " + str(message('utf-8')))
#prompt user to select a mode
print("please select a mode between modes 1-4.")

read(input)

if input == 1:
    hide_dekey()
elif input == 2: 
    find_dekey()
elif input == 3:
    hide_deway()
elif input == 4:
    show_deway()