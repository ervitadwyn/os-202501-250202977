# Mini Simulasi Sistem Operasi  
CPU Scheduling, Page Replacement, dan Deadlock Detection

## Deskripsi Proyek
Aplikasi ini merupakan mini simulasi sistem operasi berbasis terminal yang dibuat untuk
mengimplementasikan dan mendemokan beberapa konsep utama Sistem Operasi, yaitu:

- CPU Scheduling (FCFS dan SJF Non-Preemptive)
- Page Replacement (FIFO dan LRU)
- Deadlock Detection

Aplikasi dijalankan melalui Command Line Interface (CLI) dan dikemas menggunakan Docker
agar dapat dijalankan pada berbagai sistem dengan environment yang konsisten.

---

## Struktur Folder
code/
├─ main.py # Program utama (menu CLI)
├─ scheduling.py # Modul CPU Scheduling
├─ pagereplacement.py # Modul Page Replacement
├─ deadlock.py # Modul Deadlock Detection
├─ Dockerfile # Konfigurasi Docker
├─ README.md # Dokumentasi penggunaan
└─ data/
├─ scheduling.csv # Dataset CPU Scheduling
├─ pages.txt # Dataset Page Replacement
└─ deadlock.txt # Dataset Deadlock Detection

---

## Kebutuhan Sistem
### Menjalankan Tanpa Docker
- Python versi 3.8 atau lebih baru
- Library Python:
  - `tabulate`

Install library:
```bash
pip install tabulate

Menjalankan Dengan Docker

Docker Desktop (Windows / Linux / MacOS)

Cara Menjalankan Aplikasi
1. Menjalankan Secara Lokal (Tanpa Docker)

Masuk ke folder code, lalu jalankan:

python main.py

2. Menjalankan Menggunakan Docker (Disarankan)
a. Build Docker Image

Pastikan berada di folder code (yang berisi Dockerfile):

docker build -t os-simulator .

b. Menjalankan Container

docker run -it os-simulator

Jika berhasil, akan muncul menu utama aplikasi.

=== MINI SIMULASI SISTEM OPERASI ===
1. CPU Scheduling (FCFS & SJF)
2. Page Replacement (FIFO & LRU)
3. Deadlock Detection
0. Keluar

Modul dan Cara Penggunaan
1. CPU Scheduling

Modul ini mensimulasikan algoritma:

First Come First Served (FCFS)

Shortest Job First (SJF) Non-Preemptive

Input:

Dataset diambil dari file data/scheduling.csv

Output:

Tabel waiting time dan turnaround time setiap proses

Perbandingan hasil FCFS dan SJF

2. Page Replacement

Modul ini mensimulasikan algoritma:

FIFO

LRU

Input:

Dataset page reference dari file data/pages.txt

Jumlah frame dimasukkan oleh pengguna saat program berjalan

Output:

Jumlah page fault masing-masing algoritma

Perbandingan FIFO dan LRU

3. Deadlock Detection

Modul ini mendeteksi deadlock berdasarkan:

Allocation Matrix

Request Matrix

Available Resources

Input:

Dataset deadlock dari file data/deadlock.txt

Output:

Status sistem (Deadlock / Tidak Deadlock)

Daftar proses yang terlibat deadlock (jika ada)

