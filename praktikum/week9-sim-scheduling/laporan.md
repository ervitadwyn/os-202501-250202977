
# Laporan Praktikum Minggu IX
Topik: Simulasi Algoritma Penjadwalan CPU
---

## Identitas
- **Nama**  : Ervita Dwi Riyanti
- **NIM**   : 250202977
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
Dasar Teori

1. Penjadwalan CPU
Penjadwalan CPU adalah mekanisme sistem operasi untuk mengatur urutan eksekusi proses yang berada dalam keadaan siap (ready).

2. Algoritma First Come First Served (FCFS)
FCFS merupakan algoritma penjadwalan non-preemptive yang mengeksekusi proses berdasarkan urutan kedatangan.

3. Waiting Time dan Turnaround Time
Waiting time adalah waktu tunggu proses sebelum dieksekusi, sedangkan turnaround time adalah total waktu sejak proses datang hingga selesai.

4. Kelebihan dan Keterbatasan FCFS
FCFS mudah diimplementasikan namun memiliki kelemahan berupa convoy effect, di mana proses dengan burst time panjang dapat memperlambat proses lain.

5. Simulasi Komputasional Penjadwalan
Simulasi penjadwalan CPU menggunakan program komputer bertujuan untuk mengotomatisasi perhitungan manual, mempermudah analisis kinerja algoritma, serta memvalidasi hasil perhitungan teoritis melalui data uji.

---

## C. Ketentuan Teknis
- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).  
- Tidak wajib GUI, cukup **program berbasis terminal**.  
- Fokus penilaian pada **logika algoritma dan keakuratan hasil**, bukan kompleksitas bahasa.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## D. Langkah Pengerjaan
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---
## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/screenshot.png)
## Alur Program
Program simulasi dibuat menggunakan bahasa Python dengan alur sebagai berikut:
1. Membaca dataset dari file CSV.
2. Mengurutkan proses berdasarkan arrival time.
3. Menjalankan simulasi FCFS.
4. Menghitung waiting time dan turnaround time untuk setiap proses.
5. Menampilkan hasil dalam bentuk tabel pada terminal.
---
## Hasil Simulasi
Hasil simulasi menunjukkan nilai waiting time dan turnaround time sebagai berikut:

| Proses | Waiting Time | Turnaround Time |
|------|--------------|-----------------|
| P1   | 0            | 6               |
| P2   | 5            | 13              |
| P3   | 12           | 19              |
| P4   | 18           | 21              |

Rata-rata waiting time adalah **8.75** dan rata-rata turnaround time adalah **14.75**.


## Kode / Perintah
Kode yang di gunakan:
```bash
import csv

def read_dataset(filename):
    processes = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append({
                'process': row['Process'],
                'arrival': int(row['ArrivalTime']),
                'burst': int(row['BurstTime'])
            })
    return processes

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival'])

    current_time = 0
    results = []

    for p in processes:
        if current_time < p['arrival']:
            current_time = p['arrival']

        start_time = current_time
        waiting_time = start_time - p['arrival']
        turnaround_time = waiting_time + p['burst']
        finish_time = start_time + p['burst']

        results.append({
            'Process': p['process'],
            'Arrival': p['arrival'],
            'Burst': p['burst'],
            'Waiting': waiting_time,
            'Turnaround': turnaround_time
        })

        current_time = finish_time

    return results

def print_table(results):
    print("\nHasil Simulasi FCFS Scheduling")
    print("-" * 60)
    print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Waiting':<10}{'Turnaround':<10}")
    print("-" * 60)

    total_waiting = 0
    total_turnaround = 0

    for r in results:
        total_waiting += r['Waiting']
        total_turnaround += r['Turnaround']
        print(f"{r['Process']:<10}{r['Arrival']:<10}{r['Burst']:<10}{r['Waiting']:<10}{r['Turnaround']:<10}")

    avg_waiting = total_waiting / len(results)
    avg_turnaround = total_turnaround / len(results)

    print("-" * 60)
    print(f"Rata-rata Waiting Time     : {avg_waiting:.2f}")
    print(f"Rata-rata Turnaround Time  : {avg_turnaround:.2f}")

if __name__ == "__main__":
    dataset = read_dataset("dataset.csv")
    results = fcfs_scheduling(dataset)
    print_table(results)

```
---
## Analisis

Hasil simulasi sesuai dengan perhitungan manual yang telah dilakukan pada praktikum
minggu sebelumnya. Algoritma FCFS memiliki kelebihan yaitu mudah diimplementasikan
dan adil berdasarkan urutan kedatangan. Namun, algoritma ini memiliki kelemahan
berupa kemungkinan terjadinya *convoy effect*, di mana proses dengan burst time
panjang dapat memperlambat proses lain.

---
## Kesimpulan
Simulasi FCFS berhasil diimplementasikan dengan baik dan memberikan hasil yang
konsisten dengan teori. Praktikum ini membantu memahami hubungan antara konsep
penjadwalan CPU dan implementasi komputasionalnya.




## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
   **Jawaban:**
 Simulasi diperlukan untuk mengotomatisasi perhitungan penjadwalan CPU sehingga hasil lebih cepat, konsisten, dan minim kesalahan dibandingkan perhitungan manual.
3. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   **Jawaban:**
  Secara teori hasilnya sama, namun pada dataset besar simulasi jauh lebih efisien dan akurat, sedangkan perhitungan manual tidak praktis dan rawan kesalahan.
5. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
   **Jawaban:**
 Algoritma FCFS lebih mudah diimplementasikan karena hanya mengurutkan proses berdasarkan waktu kedatangan tanpa logika tambahan seperti pemilihan proses terpendek.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
