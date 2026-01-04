
# Laporan Praktikum Minggu XI
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Ervita Dwi Riyanti
- **NIM**   : 250202977
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.
---

## Dasar Teori

1. Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu resource yang sedang digunakan proses lain, sehingga tidak ada proses yang dapat melanjutkan eksekusi.

2. Empat Kondisi Deadlock. Deadlock terjadi apabila mutual exclusion, hold and wait, no preemption, dan circular wait terpenuhi secara bersamaan.

3. Deteksi deadlock dilakukan dengan menganalisis alokasi dan permintaan resource untuk menentukan apakah terdapat proses yang tidak dapat diselesaikan, yang menandakan terjadinya deadlock.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Ketentuan Teknis
- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).  
- Program berbasis **terminal**, tidak memerlukan GUI.  
- Fokus penilaian pada **logika algoritma deteksi deadlock**, bukan kompleksitas bahasa.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week11-deadlock-detection/
├─ code/
│  ├─ deadlock_detection.*
│  └─ dataset_deadlock.csv
├─ screenshots/
│  └─ hasil_deteksi.png
└─ laporan.md
```

---

## Langkah Pengerjaan
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_deteksi.png)

---

## Analisis
Tabel hasil deteksi :
| Proses | Resource Dialokasikan | Resource Diminta | Status   |
| ------ | --------------------- | ---------------- | -------- |
| P1     | R1                    | R2               | Deadlock |
| P2     | R2                    | R3               | Deadlock |
| P3     | R3                    | R1               | Deadlock |

Seluruh proses dalam status deadlock.
Deadlock terjadi karena setiap proses saling menunggu resource yang sedang dipegang oleh proses lain, sehingga tidak ada satu pun proses yang dapat melanjutkan eksekusi.

Secara rinci:

a. Proses P1 memegang resource R1 dan menunggu R2 yang sedang dipegang oleh P2

b. Proses P2 memegang resource R2 dan menunggu R3 yang sedang dipegang oleh P3

c. Proses P3 memegang resource R3 dan menunggu R1 yang sedang dipegang oleh P1

Kondisi ini membentuk circular wait, sehingga sistem mengalami kebuntuan permanen (deadlock).

Berdasarkan teori sistem operasi, deadlock terjadi apabila keempat kondisi berikut terpenuhi secara bersamaan. Pada kasus ini, seluruh kondisi tersebut terpenuhi:

1. Mutual Exclusion

Resource bersifat eksklusif, artinya hanya dapat digunakan oleh satu proses pada satu waktu. Terpenuhi, karena R1, R2, dan R3 tidak dapat dibagi.

2. Hold and Wait

Proses memegang satu resource sambil menunggu resource lain. Terpenuhi, karena setiap proses memegang satu resource dan menunggu resource berikutnya.

3. No Preemption

Resource tidak dapat direbut secara paksa dari proses yang sedang menggunakannya. Terpenuhi, karena resource hanya dilepas setelah proses selesai.

4. Circular Wait

Terdapat siklus ketergantungan antar proses. Terpenuhi, karena P1 → P2 → P3 → P1.
---

Karena keempat kondisi deadlock terpenuhi secara simultan dan tidak terdapat proses yang dapat dieksekusi hingga selesai, maka sistem berada dalam kondisi deadlock. Program deteksi deadlock berhasil mengidentifikasi proses-proses yang terlibat dalam deadlock secara tepat.

Solusi pencegahan deadlock
Deadlock dapat dicegah dengan menghilangkan salah satu dari empat kondisi deadlock. Pada kasus ini, penerapan resource ordering untuk mencegah circular wait merupakan solusi paling efektif. Alternatif lain adalah penggunaan algoritma penghindaran seperti Banker atau pendekatan deteksi dan pemulihan dengan menghentikan salah satu proses yang terlibat.

## Kesimpulan
Praktikum ini berhasil mensimulasikan dan mendeteksi kondisi deadlock pada sistem operasi menggunakan pendekatan algoritmik berbasis alokasi dan permintaan resource.
Hasil pengujian menunjukkan bahwa deadlock terjadi ketika seluruh proses saling menunggu resource yang sedang dipegang proses lain, sehingga tidak ada proses yang dapat diselesaikan.
Deteksi deadlock dapat digunakan sebagai dasar analisis untuk memahami penyebab deadlock, meskipun solusi pencegahan atau penghindaran tidak diimplementasikan dalam praktikum ini.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?
   **Jawaban:**
   Deadlock prevention bertujuan mencegah deadlock dengan menghilangkan salah satu dari empat kondisi deadlock sejak awal. Deadlock avoidance menghindari deadlock dengan memastikan sistem selalu berada dalam kondisi aman sebelum resource dialokasikan. Sementara itu, deadlock detection membiarkan sistem berjalan normal dan mendeteksi deadlock setelah terjadi untuk kemudian dilakukan pemulihan.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
   **Jawaban:**
   Deteksi deadlock diperlukan karena pada sistem yang kompleks dan dinamis, pencegahan atau penghindaran deadlock tidak selalu dapat diterapkan. Pendekatan deteksi memberikan fleksibilitas yang lebih tinggi dengan menangani deadlock hanya ketika kondisi tersebut benar-benar terjadi.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   **Jawaban:**
   Kelebihan pendekatan deteksi deadlock adalah fleksibilitas dan efisiensi penggunaan resource karena tidak membatasi permintaan proses. Namun, kekurangannya adalah deadlock dibiarkan terjadi terlebih dahulu dan adanya overhead tambahan untuk proses deteksi dan pemulihan. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
