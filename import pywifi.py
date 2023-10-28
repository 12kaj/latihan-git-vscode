import pywifi
from pywifi import const

# Membuat objek pembungkus
wifi = pywifi.PyWiFi()

# Mendapatkan antarmuka Wi-Fi yang aktif
iface = wifi.interfaces()[0]

# Mematikan semua koneksi Wi-Fi yang ada
iface.disconnect()
pywifi.sleep(1)

# Memeriksa status Wi-Fi
if iface.status() == const.IFACE_DISCONNECTED:
    # Mencari daftar jaringan Wi-Fi yang tersedia
    iface.scan()
    pywifi.sleep(5)
    networks = iface.scan_results()

    # Menampilkan daftar jaringan Wi-Fi yang tersedia
    for network in networks:
        print("SSID:", network.ssid)

    # Mengambil SSID dari pengguna
    ssid = input("Masukkan SSID Wi-Fi yang ingin dihubungkan: ")
    password = input("Masukkan kata sandi Wi-Fi: ")

    # Membuat profil Wi-Fi baru
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    # Menambahkan profil ke antarmuka Wi-Fi
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    # Menghubungkan ke jaringan Wi-Fi
    iface.connect(tmp_profile)
    pywifi.sleep(5)

    # Memeriksa status koneksi
    if iface.status() == const.IFACE_CONNECTED:
        print("Koneksi Wi-Fi berhasil!")
    else:
        print("Gagal terhubung ke Wi-Fi.")
