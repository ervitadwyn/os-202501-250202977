## LAPORAN PROYEK PRAKTIKUM 

## Mini Simulasi Sistem Operasi
Integrasi CPU Scheduling, Page Replacement, dan Deadlock Detection

### 1. Pendahuluan
**1.1 Latar Belakang**

Sistem Operasi (Operating System) merupakan komponen fundamental dalam sebuah sistem komputer yang berfungsi sebagai pengelola utama seluruh sumber daya perangkat keras (hardware) dan perangkat lunak (software). Sistem operasi bertanggung jawab dalam mengatur eksekusi proses, pengalokasian memori, pengelolaan resource, serta memastikan bahwa sistem berjalan secara efisien, aman, dan stabil.

Dalam mata kuliah Sistem Operasi, mahasiswa mempelajari berbagai konsep inti seperti penjadwalan CPU, manajemen memori, dan penanganan deadlock. Konsep-konsep tersebut biasanya dipelajari secara terpisah melalui teori dan praktikum mingguan. Namun, dalam sistem nyata, seluruh mekanisme tersebut saling terintegrasi dan bekerja secara bersamaan.

Oleh karena itu, diperlukan sebuah proyek integratif yang mampu menyatukan berbagai konsep sistem operasi ke dalam satu aplikasi simulasi sederhana agar mahasiswa dapat memahami hubungan antar konsep secara lebih komprehensif. Proyek Praktikum Minggu ke-15 ini dirancang untuk memenuhi kebutuhan tersebut melalui pembangunan mini simulasi sistem operasi berbasis terminal yang dapat dijalankan secara konsisten menggunakan Docker.

**1.2 Tujuan Proyek**

Tujuan utama dari proyek ini adalah:

Memberikan pemahaman praktis mengenai implementasi konsep sistem operasi.

Mengintegrasikan beberapa algoritma sistem operasi ke dalam satu aplikasi.

Mensimulasikan perilaku sistem operasi dalam mengatur CPU, memori, dan resource.

Melatih mahasiswa bekerja secara kolaboratif dalam tim.

Membiasakan penggunaan Git dalam pengembangan perangkat lunak.

Menggunakan Docker untuk menciptakan environment yang reproducible.

Menyajikan hasil simulasi dalam bentuk tabel dan metrik yang terukur.

### 2. Ruang Lingkup Proyek

Proyek ini mencakup pengembangan aplikasi simulasi sistem operasi dengan batasan sebagai berikut:

1. Aplikasi berbasis Command Line Interface (CLI)

2. Bahasa pemrograman yang digunakan: Python

3. Input berasal dari dataset sederhana (file teks/CSV)

4. Output berupa tabel ASCII dan ringkasan metrik

5. Dijalankan secara lokal maupun melalui Docker Container

6. Modul yang diimplementasikan meliputi:

7. CPU Scheduling

8. Page Replacement

9. Deadlock Detection (tanpa deadlock)

### 3. Metodologi dan Pendekatan Pengembangan
**3.1 Metode Pengembangan**

Metode pengembangan yang digunakan adalah pendekatan modular, di mana setiap fitur utama sistem operasi diimplementasikan dalam modul terpisah. Pendekatan ini memudahkan pengujian, pemeliharaan, dan integrasi antar modul.

**3.2 Kolaborasi Tim**

Pengembangan proyek dilakukan secara kolaboratif menggunakan Git dengan pembagian branch berdasarkan fitur. Setiap anggota tim memiliki kontribusi minimal satu fitur atau dokumentasi.

### 4. Arsitektur Aplikasi
**4.1 Desain Arsitektur Sistem**

Aplikasi terdiri dari satu program utama (main.py) yang berfungsi sebagai pengontrol alur aplikasi dan antarmuka pengguna. Modul-modul sistem operasi dipanggil berdasarkan pilihan menu yang dipilih oleh pengguna.

Secara umum, arsitektur aplikasi mengikuti pola berikut:

User → CLI Menu → Modul OS → Perhitungan → Output Tabel

**4.2 Struktur Folder Proyek**
week15-proyek-kelompok/
├─ code/
│  ├─ main.py
│  ├─ scheduling.py
│  ├─ pagereplacement.py
│  ├─ deadlock.py
│  ├─ Dockerfile
│  ├─ README.md
│  └─ data/
│     ├─ scheduling.csv
│     ├─ pages.txt
│     └─ deadlock.txt
├─ screenshots/
│  ├─ demo_run.png
│  └─ hasil_tabel.png
└─ laporan.md

**4.3 Alur Eksekusi Program**

1. Program dijalankan oleh pengguna melalui terminal.

2. Program menampilkan menu utama.

3. Pengguna memilih modul yang ingin dijalankan.

4. Program membaca dataset dari file.

5. Algoritma dijalankan sesuai modul.

6. Hasil simulasi ditampilkan dalam bentuk tabel.

7. Program kembali ke menu utama atau keluar.

### 5. Implementasi Modul Sistem Operasi
**5.1 Modul CPU Scheduling**
**5.1.1 Deskripsi Modul**

Modul CPU Scheduling bertujuan untuk mensimulasikan bagaimana sistem operasi mengatur eksekusi proses pada CPU.

**5.1.2 Algoritma yang Digunakan**

First Come First Serve (FCFS)
Proses dieksekusi berdasarkan urutan kedatangan.

Shortest Job First (SJF) Non-Preemptive
Proses dengan burst time terpendek dieksekusi terlebih dahulu.

**5.1.3 Parameter dan Output**

Input:
| Parameter    | Keterangan                          |
| ------------ | ----------------------------------- |
| Arrival Time | Waktu kedatangan proses ke sistem   |
| Burst Time   | Lama waktu eksekusi proses pada CPU |

Output:

| Parameter                 | Keterangan                                                |
| ------------------------- | --------------------------------------------------------- |
| Waiting Time              | Waktu tunggu proses sebelum dieksekusi CPU                |
| Turnaround Time           | Total waktu proses sejak datang hingga selesai dieksekusi |
| Rata-rata Waiting Time    | Nilai rata-rata waktu tunggu seluruh proses               |
| Rata-rata Turnaround Time | Nilai rata-rata turnaround time seluruh proses            |

**5.2 Modul Page Replacement**
**5.2.1 Deskripsi Modul**

Modul ini mensimulasikan manajemen memori virtual ketika terjadi page fault.

**5.2.2 Algoritma yang Digunakan**

FIFO

LRU

**5.2.3 Metrik Evaluasi**

Page Fault

Page Hit

Hit Ratio

**5.3 Modul Deadlock Detection**
**5.3.1 Deskripsi Modul**

Modul Deadlock Detection digunakan untuk mengevaluasi apakah sistem berada dalam kondisi deadlock berdasarkan resource yang dialokasikan dan diminta oleh proses.

**5.3.2 Dataset yang Digunakan (Tanpa Deadlock)**

Allocation Matrix

| Proses | R0 | R1 |
| ------ | -- | -- |
| P0     | 1  | 0  |
| P1     | 0  | 1  |


Request Matrix

| Proses | R0 | R1 |
| ------ | -- | -- |
| P0     | 0  | 0  |
| P1     | 0  | 0  |


Available Vector

| R0 | R1 |
| -- | -- |
| 1  | 1  |


### 6. Pengujian dan Hasil
**6.1 Hasil CPU Scheduling**
![Screenshot hasil](screenshots/FCFS_SJF.png)
| Proses | Waiting Time | Turnaround Time |
| ------ | ------------ | --------------- |
| P1     | 0            | 5               |
| P2     | 4            | 7               |
| P3     | 6            | 14              |


Rata-rata Waiting Time: 3.33
Rata-rata Turnaround Time: 8.67

Analisis:
Algoritma FCFS menunjukkan waktu tunggu yang meningkat untuk proses yang datang belakangan, terutama ketika terdapat proses dengan burst time panjang.

**6.2 Hasil Page Replacement**
![Screenshot hasil](screenshots/Page_Replacement_dan_Deadlock.png)
| Algoritma | Page Fault | Page Hit | Hit Ratio |
| --------- | ---------- | -------- | --------- |
| FIFO      | 9          | 3        | 0.25      |
| LRU       | 8          | 4        | 0.33      |

Analisis:
LRU memberikan performa yang lebih baik karena mempertimbangkan pola penggunaan memori sebelumnya.

**6.3 Hasil Deadlock Detection**
NO DEADLOCK DETECTED
All processes can finish safely.

| Aspek           | Hasil          |
| --------------- | -------------- |
| Status Sistem   | Tidak Deadlock |
| Safe State      | Ya             |
| Circular Wait   | Tidak          |
| Proses Terlibat | Tidak ada      |

### 7. Demo Aplikasi
**7.1 Demo Lokal**
```
python main.py
```

**7.2 Demo Menggunakan Docker**
```
docker build -t os-simulator .
```
![Screenshot hasil](screenshots/build_docker.png)
```
docker run -it os-simulator
```
![Screenshot hasil](screenshots/docker_run.png)



### 8. Pembagian Peran Tim
| No | Nama Anggota          | Peran        | Tanggung Jawab                                                                      |
| -- | --------------------- | ------------ | ----------------------------------------------------------------------------------- |
| 1  | Ervita Dwi Riyanti    | Project Lead | Koordinasi tim, integrasi seluruh modul, pengelolaan repository Git, dan merge kode |
| 2  | Syahrul Nuzulul Qori  | Developer    | Implementasi modul CPU Scheduling (FCFS dan SJF non-preemptive)                     |
| 3  | Akhmad Raffi Sarmadan | Developer    | Implementasi modul Page Replacement (FIFO dan LRU) serta Deadlock Detection         |
| 4  | Saskia Istiqomah      | Dokumentasi  | Penyusunan README.md, penulisan laporan proyek, dan pengujian aplikasi              |

### 9. Kesimpulan

Berdasarkan hasil perancangan, implementasi, dan pengujian yang telah dilakukan, dapat disimpulkan bahwa proyek Mini Simulasi Sistem Operasi ini berhasil mengintegrasikan beberapa konsep utama sistem operasi ke dalam satu aplikasi simulasi berbasis terminal. Modul CPU Scheduling, Page Replacement, dan Deadlock Detection dapat bekerja secara terpadu dalam mengelola sumber daya sistem. Pada modul CPU Scheduling, algoritma FCFS dan SJF non-preemptive berhasil disimulasikan sesuai teori, di mana FCFS menunjukkan kelemahan berupa meningkatnya waktu tunggu pada proses yang datang belakangan, sedangkan SJF mampu memberikan waktu tunggu rata-rata yang lebih rendah dengan memprioritaskan proses berdurasi terpendek. Pada modul Page Replacement, algoritma LRU terbukti lebih efisien dibandingkan FIFO karena menghasilkan jumlah page fault yang lebih rendah dan hit ratio yang lebih tinggi, sesuai dengan konsep pengelolaan memori virtual yang mempertimbangkan riwayat penggunaan page.

Pada modul Deadlock Detection, pengujian menggunakan dataset dalam kondisi aman (safe state) menunjukkan bahwa sistem tidak mengalami deadlock dan seluruh proses dapat menyelesaikan eksekusinya dengan baik. Hal ini membuktikan bahwa algoritma deteksi deadlock mampu mengidentifikasi kondisi sistem secara tepat, baik dalam keadaan aman maupun tidak. Selain keberhasilan teknis, proyek ini juga memberikan pengalaman penting dalam kerja tim dan manajemen proyek perangkat lunak melalui penggunaan Git sebagai alat kolaborasi dan Docker sebagai media deployment untuk memastikan lingkungan eksekusi yang konsisten. Secara keseluruhan, proyek ini telah memenuhi tujuan praktikum dan berkontribusi dalam meningkatkan pemahaman konseptual serta keterampilan praktis mahasiswa dalam bidang sistem operasi dan pengembangan perangkat lunak.
