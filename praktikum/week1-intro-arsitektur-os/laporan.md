
# Laporan Praktikum Minggu I
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : ERVITA DWI RIYANTI
- **NIM**   : 250202977 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Sistem Operasi(OS) adalah software yang mengatur seluruh aktifitas hardware dan software pada komputer. Sistem Operasi juga yang menghubungkan antara user dan hardware yang memungkinkan user berinteraksi dan menjalankan aplikasi. Salah satu bagian terpentingnya adalah Kernel, yaitu inti Sistem Operasi yang mengelola sumber daya seperti : CPU, Hardisk/SSD/Memori, dan perangkat I/O.
- Linux merupakan sistem operasi berbasis kernel monolithic yang bersifat open source.
- Windows Subsystem for Linux (WSL) adalah fitur bawaan windows yang memungkinkan pengguna menjalankan lingkungan Linux secara langsung di atas Windows tanpa perlu mesin virtual/dualboot. WSL dapat menerjemahkan systemcall Linux agar kompatibel dengan kernel Windows.
- Percobaan ini bertujuan mengenal konsep kernel, sistem operasi berbasis Linux, serta memahami cara kerja WSL sebagai jembatan antara OS Windows dan Liux.

---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Makna hasil percobaan
  Dari hasil percobaan tersebut, dapat di peroleh bahwa instalasi WSL berhasil menciptakan lingkungan Linux di dalam sistem operasi Windows tanpa perlu dual boot/virtual machine. Perintah yang saya coba seperti :
  ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
menunjukan bahwa kernel Linux aktif dan dapat berinteraksi dengan user melalui terminal. Membuktikan bahwa Windows mampu menjalankan sistem Linux secara langsung dengan memanfaatkan lapisan hubungan kernel yang di sediakan WSL.

- Hubungan hasil dengan teori
  Fungsi Kernel sebagai inti sistem operasi yang mengatur komunikasi antara hardware dan software. Saat perintah di jalankan user dapat melihat bagaimana kernel memuat modul dan mengelola pesan sistem. Peran Kernel sebagai pengendali sistem. Ketika user menjalankan perintah di terminal sistem akan melakukan system call ke kernel untuk meminta layanan seperti membaca memori, menampilkan proses, dan mengakses perangkat. WSL menerjemahkan system call Linux agar dapat di jalankan di atas kernel Windows. Hasil Percobaan terlihat konsep arsitektur Sistem Operasi, dimana WSL berperan sebagai lapisan kompatibilitas antara Windows dan Linux. Kernel Linux beroperasi secara virtual di atas kernel Windows tanpa tabrakan secara langsung dengan hardware. 
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  1. Kernel
     Linux      : Berjalan langsung di atas Hardware
     WSL        : Dijalankan secara virtual di atas kernel Windows
  2. Akses Hardware
     Linux      : Langsung ke hardware
     WSL        : Akses terbatas tergantung izin dari Windows
  3. Kinerja
     Linux      : Lebih cepat, tidak ada lapisan transisi
     WSL        : Sedikit lebih lambat, ada lapisan WSL
  4. System Call
     Linux      : Dijalankan oleh kernel Linux
     WSL        : Diterjemahkan ke kernel Windows
  5. Fleksibilitas
     Linux      : Dapat mengubah kernel dan modul sendiri
     WSL        : Kernel di kontrol oleh Windows

     
---

## Kesimpulan
- Instalasi WSL berhasil menciptakan lingkungan kerja Linux di dalam Windows, sehingga user dapat menjalankan perintah dan aplikasi Linux secara langsung.
- Peran Kernel sebagai inti sistem operasi yang mengatur komunikasi antara hardware dan software, serta mengenali konsep system call dan arsitektur berlapis dalam sistem operasi.
- Meskipun WSL tidak menjalankan kernel Linux secara penuh seperti sistem Linux asli, hasil percobaan menunjukan bahwa hubungan antara Windows dan Linux melalui WSL tetap efisien dan fungsional untuk pengembangan maupun pembelajaran sistem operasi.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.
    **Jawaban: Managemen sumber daya, Management Proses, dan managemt sistem file dan antarmuka user.**  
2. Jelaskan perbedaan antara *kernel mode* dan *user mode*.
    **Jawaban:Perbedaan antara kernel mode dan user mode yaitu terletak pada : Hak akses yaitu Kernel mode memiliki akses penuh ke seluruh sumber daya sistem sedangkan User Mode memiliki akses yang terbatas dan tidak langsung ke hardware, Kegunaan yaitu Karnel Mode Digunakan untuk menjalankan bagian inti OS sedangkan User Mode digunakan oleh aplikasi dan program pengguna, Resiko Kesalahan pada Karnel Mode kesalahan bisa menyebabkan sistem crash sedangkan pada User Mode kesalaha hanya mempengaruhi Aplikasi tersebut, dan pada contoh aktivitas dari kernel mode yaitu msalah satunya mengelola memori sedangkan User Mode Menjalankan Browser, text editor, dan terminal. Dapat di simpulkan bahwa Kernel mode untuk sistem operasi dan User Mode untuk aplikasi pengguna.** 
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
    **Jawaban:
   Contoh OS pada Monolithic   :   - Linux
                                   - MS-DOS
                                   - Unix Tradisional
   Contoh OS pada Microkernel  :   - Minix
                                   - QNX
                                   - Mach** 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Hal yang saya rasakan dan paling menantang pada minggu ini yaitu pada bagian dimana saya belajar proses instalasi dan konfigurasi WSL, karena saya harus memahami hubungan antara Windows dan Linux sebelum saya menjalankan programnya, karena sebelumnya saya belum pernah mencoba menggunakan Ubuuntu, saya merasa tertantang tetapi sedikit takut dan was was karena saya mencobanya menggunakan laptop pribadi, sebelum itu saya mencoba untuk memahami konsep kernel dan system call sebelum saya memulai praktikum, meskipun hasil percobaan berjalan dengan baik tetap ada rasa ragu dan bingung.
- Bagaimana cara Anda mengatasinya?
  Untuk mengatasi tantangan tersebut, saya mencari referensi dari internet seperti google, youtube dan beberapa panduan online, untuk melihat tutorial instalasi dengan benar sehingga tidak terjadi crash dan kesalahan yang lain. Dan tetap berusaha meyakinkan diri saya bahwa saya bisa.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
