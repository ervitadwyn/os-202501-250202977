
# Laporan Praktikum Minggu X
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

1. Penjadwalan CPU (CPU Scheduling)
Penjadwalan CPU adalah proses pemilihan urutan eksekusi proses oleh sistem operasi untuk memaksimalkan penggunaan CPU dan meminimalkan waktu tunggu.

2. First Come First Served (FCFS)
FCFS mengeksekusi proses berdasarkan urutan kedatangan. Sederhana dan adil, tetapi dapat menyebabkan convoy effect karena proses pendek menunggu proses panjang selesai.

3. Shortest Job First (SJF)
SJF memilih proses dengan waktu eksekusi terpendek terlebih dahulu. Memberikan waktu tunggu rata-rata paling rendah, namun sulit diterapkan karena memerlukan estimasi burst time dan berpotensi menyebabkan starvation pada proses panjang.

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

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Praktikum_FCFS_SJF_SS.png
)

**Eksperimen 1**

Gantt Chart

Skenario 1

FCFS
 ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
 ```

SJF
 ```
     | P4 | P1 | P3 | P2 |
     3    6    12   19   27
 ```
Skenario 2

FCFS
 ```
     | P1 | P2 | P3 | P4 |
     1    8    17   25   29
 ```
SJF
 ```
     | P4 | P1 | P3 | P2 |
     4    8    15   23   31
 ```

**Eksperimen 2**

Skenario 1

 | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
 |------------|------------------|----------------------|------------|-------------|
 | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
 | SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |
     

Skenario 2

 | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
 |------------|------------------|----------------------|------------|-------------|
 | FCFS | 10,25 | 17,25 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
 | SJF | 10 | 17 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

---

## Analisis

Berdasarkan hasil simulasi, algoritma SJF menghasilkan kinerja yang sedikit lebih baik dibanding FCFS, karena mampu meminimalkan waktu tunggu (WT) dan turnaround time (TAT) rata-rata.
Secara teori, SJF memang dirancang untuk meminimalkan waktu tunggu rata-rata, walaupun lebih sulit diterapkan secara real-time karena harus mengetahui burst time setiap proses sebelumnya.

1. Kondisi di mana SJF lebih unggul dari FCFS

Algoritma SJF (Shortest Job First) akan lebih unggul dan efisien ketika sistem memiliki proses dengan variasi burst time yang cukup besar, artinya ada proses dengan waktu eksekusi yang sangat singkat dan ada yang cukup panjang. Dalam situasi seperti ini, SJF dapat menurunkan rata-rata waktu tunggu (Waiting Time) dan waktu penyelesaian (Turnaround Time) karena proses-proses yang lebih pendek diselesaikan terlebih dahulu, sehingga antrian proses tidak tertahan oleh proses yang panjang.
Selain itu, SJF juga sangat efektif pada sistem batch processing atau sistem yang burst time-nya sudah diketahui sebelumnya, seperti pada simulasi atau sistem non-interaktif. Dengan begitu, sistem dapat mengatur urutan proses dengan tepat untuk mendapatkan efisiensi maksimal. Secara umum, SJF memberikan kinerja terbaik dalam hal minimasi waktu tunggu rata-rata dan meningkatkan throughput sistem.

2. Kondisi di mana FCFS lebih unggul dari SJF

Sebaliknya, algoritma FCFS (First Come First Served) lebih unggul dan sesuai digunakan pada sistem yang sederhana, di mana setiap proses diperlakukan secara adil berdasarkan urutan kedatangan tanpa memperhatikan lama waktu eksekusi. FCFS lebih cocok untuk lingkungan interaktif atau sistem real-time yang menuntut keadilan (fairness) dan kepastian urutan eksekusi.
FCFS juga lebih mudah diimplementasikan karena tidak memerlukan informasi tambahan seperti burst time proses. Pada kondisi di mana seluruh proses memiliki burst time yang hampir sama, maka performa FCFS dan SJF akan relatif setara, sehingga FCFS menjadi pilihan praktis dengan kompleksitas rendah.

Namun, perlu diperhatikan bahwa FCFS memiliki kelemahan utama, yaitu kondisi ketika proses dengan burst time panjang datang lebih awal dan membuat proses-proses lain menunggu terlalu lama. Dalam situasi ini, SJF jelas lebih efisien.


---

## Kesimpulan
SJF lebih unggul saat sistem memiliki proses dengan variasi burst time yang besar dan burst time diketahui sebelumnya, karena mampu meminimalkan waktu tunggu rata-rata.
Sedangkan FCFS lebih unggul pada sistem sederhana yang membutuhkan keadilan urutan eksekusi dan tidak memerlukan pengetahuan tentang burst time setiap proses.

---
## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  

Skenario 1

 | Algoritma | Avg Waiting Time | Avg Turnaround Time |
 |------------|------------------|----------------------|
 | FCFS | 8,75 | 14,75 |
 | SJF | 8,5 | 14,5 |
 
Skenario 2

 | Algoritma | Avg Waiting Time | Avg Turnaround Time | 
 |------------|------------------|----------------------|
 | FCFS | 10,25 | 17,25 |
 | SJF | 10 | 17 |
 
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
FCFS Skenario 1

| Proses      | Arrival | Burst | Start | Finish |  Waiting | Turnaround |
| :---------- | :-----: | :---: | :---: | :----: | :------: | :--------: |
| P1          |    0    |   6   |   0   |    6   |     0    |      6     |
| P2          |    1    |   8   |   6   |   14   |     5    |     13     |
| P3          |    2    |   7   |   14  |   21   |    12    |     19     |
| P4          |    3    |   3   |   21  |   24   |    18    |     21     |
| **Average** |         |       |       |        | **8.75** |  **14.75** |

SJF Skenario 1

| Proses      | Arrival | Burst | Start | Finish | Waiting | Turnaround |
| :---------- | :-----: | :---: | :---: | :----: | :-----: | :--------: |
| P4          |    3    |   3   |   3   |    6   |    0    |      3     |
| P1          |    0    |   6   |   6   |   12   |    6    |     12     |
| P3          |    2    |   7   |   12  |   19   |    10   |     17     |
| P2          |    1    |   8   |   19  |   27   |    18   |     26     |
| **Average** |         |       |       |        | **8.5** |  **14.5**  |

FSFS Skenario 2

| Proses      | Arrival | Burst | Start | Finish |  Waiting  | Turnaround |
| :---------- | :-----: | :---: | :---: | :----: | :-------: | :--------: |
| P1          |    1    |   7   |   1   |    8   |     0     |      8     |
| P2          |    2    |   9   |   8   |   17   |     6     |     15     |
| P3          |    3    |   8   |   17  |   25   |     14    |     22     |
| P4          |    4    |   4   |   25  |   29   |     21    |     25     |
| **Average** |         |       |       |        | **10.25** |  **17.25** |

SJF Skenario 2

| Proses      | Arrival | Burst | Start | Finish | Waiting | Turnaround |
| :---------- | :-----: | :---: | :---: | :----: | :-----: | :--------: |
| P4          |    4    |   4   |   4   |    8   |    0    |      4     |
| P1          |    1    |   7   |   8   |   15   |    7    |     14     |
| P3          |    3    |   8   |   15  |   23   |    12   |     20     |
| P2          |    2    |   9   |   23  |   31   |    21   |     30     |
| **Average** |         |       |       |        |  **10** |   **17**   |

4. Analisis kelebihan dan kelemahan tiap algoritma.  

| Algoritma                          | Kelebihan                                                                                                                                                                                        | Kelemahan                                                                                                                                                                                                                   |
| :--------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FCFS (First Come First Served)** | - Sederhana dan mudah diimplementasikan.<br>- Adil karena setiap proses dilayani berdasarkan urutan kedatangan.<br>- Cocok untuk sistem batch yang beban prosesnya seragam.                      | - Tidak efisien bila ada proses dengan waktu burst panjang (terjadi **convoy effect**).<br>- Waktu tunggu rata-rata bisa tinggi.<br>- Tidak responsif untuk sistem interaktif.                                              |
| **SJF (Shortest Job First)**       | - Memiliki waktu tunggu dan turnaround rata-rata **terendah** dibanding algoritma lain.<br>- Efisien untuk sistem dengan estimasi burst time yang akurat.<br>- Mengoptimalkan throughput sistem. | - Sulit diterapkan karena waktu burst tiap proses biasanya **tidak diketahui sebelumnya**.<br>- Dapat menyebabkan **starvation** untuk proses yang memiliki burst time panjang.<br>- Kurang sesuai untuk sistem interaktif. |

5. Simpan seluruh hasil dan analisis ke `laporan.md`.  

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

  Lumayan mengalami kesulitan dalam menghitung WT dan TAT karena lumayan membingungkan.
- Bagaimana cara Anda mengatasinya?

  Mengulang dan mencoba terus proses penghitungannya, dan latihan dengan skenario yang berbeda
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
