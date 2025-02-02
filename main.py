import requests
import os
import time
from datetime import datetime, timedelta
from colorama import Fore, init
import pyfiglet
import json
import config  # Import pengaturan dari file config.py

# Inisialisasi colorama
init()

# Fungsi untuk menampilkan judul
def tampilkan_judul():
    os.system('cls' if os.name == 'nt' else 'clear')
    judul = pyfiglet.figlet_format("Jerry Madez", font="slant")
    print(Fore.BLUE + judul + Fore.RESET)
    print(Fore.GREEN + "Selamat datang di program pengirim pesan Discord!" + Fore.RESET)

# Fungsi untuk mengirim pesan
def kirim_pesan(token, channel_id, pesan):
    try:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {"Authorization": token, "Content-Type": "application/json"}  # Perubahan: Gunakan token pengguna langsung
        data = {"content": pesan}
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            print(Fore.GREEN + "Pesan berhasil dikirim!" + Fore.RESET)
            return response.json()["id"]
        else:
            print(Fore.RED + f"Gagal mengirim pesan. Kode status: {response.status_code}" + Fore.RESET)
            print(response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}" + Fore.RESET)
        return None

# Fungsi untuk menghapus pesan
def hapus_pesan(token, channel_id, message_id):
    try:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
        headers = {"Authorization": token}  # Perubahan: Gunakan token pengguna langsung
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print(Fore.GREEN + "Pesan berhasil dihapus!" + Fore.RESET)
        else:
            print(Fore.RED + f"Gagal menghapus pesan. Kode status: {response.status_code}" + Fore.RESET)
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}" + Fore.RESET)

# Contoh penggunaan program
if __name__ == "__main__":
    tampilkan_judul()

    token = config.TOKEN
    channel_id = config.CHANNEL_ID

    while True:
        try:
            with open("pesan.txt", "r", encoding="utf-8") as f:
                pesan = f.readlines()  # Baca pesan per baris

            if not pesan:  # Cek apakah file pesan.txt tidak kosong
                print(Fore.YELLOW + "File pesan.txt kosong. Menunggu 60 detik sebelum mencoba lagi." + Fore.RESET)
                time.sleep(60)
                continue  # Kembali ke awal loop

            interval = int(input(Fore.YELLOW + "Masukkan interval waktu pengiriman (detik): " + Fore.RESET))

            # Loop melalui pesan berulang kali
            while True:
                for p in pesan:
                    p = p.strip()  # Hapus spasi awal dan akhir baris
                    waktu_kirim = datetime.now() + timedelta(seconds=interval)
                    print(Fore.YELLOW + f"Pesan akan dikirim pada: {waktu_kirim}")

                    while datetime.now() < waktu_kirim:
                        time.sleep(1)  # Tunggu 1 detik

                    id_pesan = kirim_pesan(token, channel_id, p)
                    if id_pesan:
                        print(Fore.GREEN + f"ID pesan: {id_pesan}")
                        time.sleep(5)  # Tunda 5 detik sebelum dihapus
                        hapus_pesan(token, channel_id, id_pesan)

        except FileNotFoundError:
            print(Fore.RED + "File pesan.txt tidak ditemukan. Buat dulu file tersebut." + Fore.RESET)
            time.sleep(60)  # Tunda 1 menit sebelum mencoba lagi
        except ValueError:
            print(Fore.RED + "Input interval waktu tidak valid. Masukkan angka detik yang benar." + Fore.RESET)
            time.sleep(60)  # Tunda 1 menit sebelum mencoba lagi
        except KeyboardInterrupt:  # Tangkap Ctrl+C
            print(Fore.YELLOW + "Pengiriman pesan dihentikan." + Fore.RESET)
            break  # Keluar dari loop utama
        except Exception as e:
            print(Fore.RED + f"Terjadi kesalahan umum: {e}" + Fore.RESET)
            time.sleep(60)  # Tunda 1 menit sebelum mencoba lagi
