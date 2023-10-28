#!/usr/bin/python

import os
import getpass

#pasword
PASSWORD = "1234"

#pembersih teks
def bersih():
    os.system("clear")

def login():
    bersih()
    password = getpass.getpass("Masukkan password: ")
    if password == PASSWORD:
        
    else:
        print("Password salah. Soba lagi.")
        login()
        
if__name__== "__main__":
    login()