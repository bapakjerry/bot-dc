# Discord Auto Kirim & Hapus Pesan!

Bot Discord ini berfungsi untuk mengirim dan menghapus pesan otomatis.

## Cara Menggunakan

1.  Clone repositori ini:

    ```bash
    git clone https://github.com/bapakjerry/bot-dc.git
    ```

2. Buat dan Aktifkan Virtual Environment:

   ```bash
   apt install python3-venv
   ```
   ```bash
   python3 -m venv bot-dc
   ```
   ```bash
   source bot-dc/bin/activate
   ```

3.  Instal library yang dibutuhkan:

    ```bash
    pip install -r requirements.txt
    ```

4.  Edit file `config.py` dan isi dengan token bot dan ID channel Anda.

5.  Edit file `pesan.txt` dan isi dengan pesan yang ingin dikirim.

6.  Jalankan bot:

    ```bash
    python main.py
    ```

## Catatan

*   Pastikan Anda telah membuat akun Discord dan mendapatkan tokennya.
*   Pastikan bot Anda memiliki izin yang cukup untuk mengirim dan menghapus pesan di channel Discord.
*   Jangan pernah membagikan token Anda kepada siapa pun.
