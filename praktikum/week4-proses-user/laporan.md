
# Laporan Praktikum Minggu IV
Topik: Manajemen Proses dan User di Linux
---

## Identitas
- **Nama**  : ERVITA DWI RIYANTI  
- **NIM**   : 250202977  
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem. 

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```bash
   whoami
   id
   groups
   ```
 ```bash
     sudo adduser praktikan
     sudo passwd praktikan
 ```
 ```bash
   ps aux | head -10
   top -n 1
   ```
```bash
     sleep 1000 &
     ps aux | grep sleep
```
 ```bash
     kill <PID>
 ```
 ```bash
   pstree -p | head -20
 ```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/week4_1.png)
![Screenshot hasil](screenshots/week4_2.png)

---
## Eksperimen 1

Perintah 
``` bash
whoami
```
berfungsi menampilkan nama useryang sedang login di terminal Linux. Artinya user yang sedang masuk ke sistem dan menjalankan terminal adalah ervitadwyn. Perintah ini berguna untuk memastikan user sedang berada sebagai user biasa atau root (administrator).
```bash
id
```
Berfungsi menampilkan informasi lengkap identitas user, yaitu : UID,GID,Groups
Penjelasan:

- uid=1000(ervitadwyn) = User ID adalah 1000, nama user ervitadwyn

- gid=1000(ervitadwyn) = Group ID utama juga bernama ervitadwyn

- groups=... = Menunjukkan user ini tergabung di beberapa grup, misalnya:

   adm = bisa melihat log sistem

   cdrom = akses ke perangkat CD/DVD

   sudo = punya hak administrator (bisa jalankan perintah sudo)

   dip = akses jaringan dial-up

   plugdev = akses perangkat USB/external

   users = grup umum untuk pengguna biasa
```bash
groups
```
Berfungsi menampilkan daftar nama grup yang di ikuti oleh user saat ini tanpa menyebutkan idnya. Artinya user ervitadwyn tergabung dalam tujuh grup, termasuk sudo, sehingga bia menjalankan perintah dengan hak akses admin.

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---
Tugas & Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.  
4. Upload laporan ke repositori Git tepat waktu.

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?  
2. Apa perbedaan antara `kill` dan `killall`?  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
