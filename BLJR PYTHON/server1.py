from random import *
import os
import string

u_pwd = input("Masukkan Kata Sandi: ")

pw = ""
attempts = 0

while pw != u_pwd:
    pw = ""
    for _ in range(len(u_pwd)):
        guess_pwd = choice(string.ascii_letters + string.digits)
        pw += guess_pwd

    attempts += 1
    print(f"Percobaan ke-{attempts}: {pw}")
    print("Memecahkan Kata Sandi... Mohon tunggu!")
    os.system("cls")

print("Kata Sandi Anda adalah:", pw)
print("Total percobaan yang dibutuhkan:", attempts)
