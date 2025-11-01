
# Laporan Praktikum Minggu [X]
Topik: Penjadwalan CPU – FCFS dan SJF
---

## Identitas
- **Nama**  : ERVITA DWI RIYANTI
- **NIM**   : 250202977
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```

---

---

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
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---
## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara FCFS dan SJF?
   
   **Jawaban :**

   Pada FCFS, proses dieksekusi berdasarkan urutan kedatangannya. Artinya, proses yang datang lebih dulu akan dijalankan terlebih
   dahulu tanpa memperhatikan lama waktu eksekusinya. Algoritma ini sederhana, tetapi bisa menyebabkan proses yang memiliki waktu
   eksekusi singkat menunggu lama jika ada proses panjang datang lebih dulu.
   Sedangkan pada SJF, proses dijalankan berdasarkan waktu eksekusi yang paling pendek terlebih dahulu. Jadi, proses yang membutuhkan
   waktu paling sedikit akan diprioritaskan. Cara ini membuat waktu tunggu rata-rata menjadi lebih kecil dan sistem menjadi lebih
   efisien. Namun, kekurangannya adalah sulit diterapkan karena waktu eksekusi setiap proses harus diketahui terlebih dahulu.

3. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?
   
   **Jawaban :**
   SJF menghasilkan waktu tunggu rata-rata paling kecil karena proses dengan waktu eksekusi paling singkat dikerjakan lebih dulu,
   sehingga proses-proses cepat tidak perlu menunggu lama di belakang proses yang panjang.
   
5. Apa kelemahan SJF jika diterapkan pada sistem interaktif?

   **Jawaban :**
   
   SFJ tidak cocok untuk lingkungan yang membutuhkan respon cepat dan waktu kedatangan proses yang tidak pasti.
   Contohnya :

   - Sulit mengetahui waktu eksekusi (burst time) setiap proses di awal, padahal SJF membutuhkannya untuk menentukan prioritas.
   - Proses panjang bisa terus tertunda (starvation) jika selalu ada proses baru yang lebih pendek datang.
   - Tidak responsif terhadap permintaan pengguna secara langsung, karena proses yang baru datang bisa harus menunggu proses lain selesai.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
