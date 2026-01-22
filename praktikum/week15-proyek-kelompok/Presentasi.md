# PRESENTASI PROYEK KELOMPOK: MINI SIMULASI SISTEM OPERASI

**Topik:** CPU Scheduling (FCFS) & Memory Management (FIFO)
**Minggu:** 15

---

## Nama Anggota Kelompok

* **Ervita Dwi Riyanti** – Project Lead
* **Syahrul Nuzulul Qori** – Developer (CPU Scheduling)
* **Akhmad Raffi Sarmadan** – Developer (Page Replacement & Deadlock Detection)
* **Saskia Istiqomah** – Dokumentasi

---

## 1. PENDAHULUAN

### Latar Belakang

Konsep sistem operasi seperti CPU Scheduling, Manajemen Memori, dan Deadlock merupakan materi fundamental namun sering kali bersifat abstrak dan sulit dipahami jika hanya dipelajari secara teoritis. Mahasiswa kerap mengalami kesulitan dalam membayangkan bagaimana algoritma-algoritma tersebut bekerja secara nyata di dalam sistem komputer.

Oleh karena itu, proyek Mini Simulasi Sistem Operasi ini dikembangkan sebagai media pembelajaran berbasis simulasi agar konsep-konsep tersebut dapat divisualisasikan dan dipahami secara lebih konkret melalui eksekusi langsung di terminal.

### Tujuan Proyek

* Mensimulasikan algoritma CPU Scheduling FCFS
* Mensimulasikan algoritma Page Replacement FIFO
* Menunjukkan hasil eksekusi berupa metrik kinerja sistem
* Memberikan pemahaman praktis tentang perilaku sistem operasi

---

## 2. ARSITEKTUR APLIKASI

### Tech Stack

* **Bahasa Pemrograman:** Python (CLI / Terminal)
* **Environment:** Docker (reproducible environment)
* **Version Control:** Git

### Desain Modular

Arsitektur aplikasi dirancang secara modular agar mudah dikembangkan dan dipahami:

* **Controller Utama (`main.py`)**
  Mengatur alur program, menampilkan menu, dan memanggil modul simulasi.

* **Modul CPU Scheduling (`scheduling.py`)**
  Mengimplementasikan algoritma FCFS untuk menghitung Waiting Time dan Turnaround Time.

* **Modul Page Replacement (`pagereplacement.py`)**
  Mengimplementasikan algoritma FIFO untuk manajemen memori virtual.

* **Manajemen Data (`data/`)**
  Menyimpan dataset input dalam bentuk file teks.

---

## 3. LIVE DEMO APLIKASI

### Skenario Demo

1. **Menjalankan Aplikasi via Docker**

```bash
docker build -t os-simulator .
docker run -it --rm os-simulator
```

2. **Simulasi CPU Scheduling (FCFS)**

* Input: Arrival Time & Burst Time
* Output: Waiting Time, Turnaround Time, rata-rata waktu

3. **Simulasi Page Replacement (FIFO)**

* Input: Urutan page
* Set frame memori
* Output: Page Fault & Page Hit

---

## 4. HASIL & ANALISIS: CPU SCHEDULING (FCFS)

### Data Hasil Pengujian

| Proses | Waiting Time | Turnaround Time |
| ------ | ------------ | --------------- |
| P1     | 0            | 5               |
| P2     | 4            | 7               |
| P3     | 6            | 14              |

### Analisis

Algoritma FCFS mengeksekusi proses berdasarkan urutan kedatangan tanpa memperhatikan lama eksekusi. Hal ini dapat menyebabkan proses dengan burst time kecil harus menunggu lama jika terdapat proses besar di awal antrian.

**Kesimpulan:** FCFS sederhana dan adil secara urutan, namun kurang optimal dari sisi efisiensi waktu tunggu.

---

## 5. HASIL & ANALISIS: MEMORY MANAGEMENT (FIFO)

### Data Hasil Pengujian

| Algoritma | Page Fault | Page Hit | Hit Ratio |
| --------- | ---------- | -------- | --------- |
| FIFO      | 9          | 3        | 0.25      |
| LRU       | 8          | 4        | 0.33      |

### Analisis

FIFO mengganti page berdasarkan urutan masuk tanpa mempertimbangkan frekuensi penggunaan. Akibatnya, page yang masih sering digunakan dapat terhapus hanya karena masuk lebih awal.

**Kesimpulan:** FIFO mudah diimplementasikan tetapi kurang efisien untuk pola akses berulang.

---

## 6. HASIL & ANALISIS: DEADLOCK DETECTION

### Dataset Pengujian

**Allocation Matrix**

| Proses | R0 | R1 |
| ------ | -- | -- |
| P0     | 1  | 0  |
| P1     | 0  | 1  |

**Request Matrix**

| Proses | R0 | R1 |
| ------ | -- | -- |
| P0     | 0  | 0  |
| P1     | 0  | 0  |

**Available Vector**

| R0 | R1 |
| -- | -- |
| 1  | 1  |

### Hasil

| Aspek           | Hasil          |
| --------------- | -------------- |
| Status Sistem   | Tidak Deadlock |
| Safe State      | Ya             |
| Circular Wait   | Tidak          |
| Proses Terlibat | Tidak ada      |

---

## 7. TIM & KONTRIBUSI

| Anggota               | Peran        | Tanggung Jawab              |
| --------------------- | ------------ | --------------------------- |
| Ervita Dwi Riyanti    | Project Lead | Integrasi dan koordinasi    |
| Syahrul Nuzulul Qori  | Developer    | CPU Scheduling              |
| Akhmad Raffi Sarmadan | Developer    | Page Replacement & Deadlock |
| Saskia Istiqomah      | Dokumentasi  | README & Laporan            |

---

## 8. PENUTUP

Proyek Mini Simulasi Sistem Operasi ini berhasil mengimplementasikan konsep utama OS secara terintegrasi dan aplikatif. Melalui simulasi langsung, mahasiswa dapat memahami kelebihan dan kekurangan masing-masing algoritma serta memperoleh pengalaman praktis dalam pengembangan perangkat lunak berbasis tim dan containerisasi.

Proyek ini diharapkan dapat menjadi dasar pembelajaran yang kuat untuk materi sistem operasi lanjutan dan pengembangan sistem yang lebih kompleks di masa depan.
