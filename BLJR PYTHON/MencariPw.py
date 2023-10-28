from random import *
import os

from getpass import getpass

u_pwd = getpass("Masukkan Kata Sandi: ")
print("Kata Sandi yang Dimasukkan:", u_pwd)
pwd = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]

pw = ""
while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw = str(guess_pwd) + pw
        print(pw)
        print("Memecahkan Kata Sandi... Mohon tunggu!")
        os.system("cls")
print("Kata Sandi Anda adalah:", pw)
