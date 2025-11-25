
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas
- **Nama**  : Ervita Dwi Riyanti
- **NIM**   : 250202977
- **Kelas** : 1IKRA

---

## Tujuan

Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.  
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---
## Eksperimen 1

Simulasi Dining Philosophers (Deadlock Version)
```
import threading
import time
import random

# jumlah filsuf
N = 5

# setiap garpu = 1 lock
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.5, 1.5))

        print(f"Filsuf {i} mencoba mengambil garpu kiri {left}")
        forks[left].acquire()
        print(f"Filsuf {i} mengambil garpu kiri {left}")

        print(f"Filsuf {i} mencoba mengambil garpu kanan {right}")
        forks[right].acquire()  # <-- DI SINI DEADLOCK TERJADI
        print(f"Filsuf {i} mengambil garpu kanan {right}")

        print(f"Filsuf {i} sedang makan...")
        time.sleep(random.uniform(0.5, 1.5))

        forks[left].release()
        forks[right].release()
        print(f"Filsuf {i} selesai makan dan meletakkan garpu\n")

# Membuat thread
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
```

## Eksperimen 2
Versi Fixed (Menggunakan Semaphore / Monitor)
FIXED VERSION — Semaphore (Mutex Global)
```
import threading
import time
import random

N = 5
forks = [threading.Lock() for _ in range(N)]
mutex = threading.Semaphore(1)  # mencegah deadlock

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.2, 0.6))

        mutex.acquire()  # hanya 1 filsuf yang boleh ambil garpu
        forks[left].acquire()
        forks[right].acquire()
        mutex.release()

        print(f"Filsuf {i} mulai makan...")
        time.sleep(random.uniform(0.3, 0.7))

        forks[left].release()
        forks[right].release()
        print(f"Filsuf {i} selesai makan.\n")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
```

FIXED VERSION Batasi Maksimal 4 Filsuf

```
import threading
import time
import random

N = 5
forks = [threading.Lock() for _ in range(N)]
room = threading.Semaphore(4)   # hanya 4 boleh mencoba makan

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.2, 0.6))

        room.acquire()
        forks[left].acquire()
        forks[right].acquire()

        print(f"Filsuf {i} makan...")
        time.sleep(random.uniform(0.3, 0.7))

        forks[left].release()
        forks[right].release()
        room.release()
        print(f"Filsuf {i} selesai makan.\n")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
```

FIXED VERSION Odd–Even Fork Picking Rule

```
import threading
import time
import random

N = 5
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    left = i
    right = (i + 1) % N

    # odd = right-first, even = left-first
    first = left if i % 2 == 0 else right
    second = right if i % 2 == 0 else left

    while True:
        print(f"Filsuf {i} sedang berpikir...")
        time.sleep(random.uniform(0.2, 0.6))

        forks[first].acquire()
        forks[second].acquire()

        print(f"Filsuf {i} makan (urutan garpu dibalik)...")
        time.sleep(random.uniform(0.3, 0.7))

        forks[first].release()
        forks[second].release()
        print(f"Filsuf {i} selesai makan.\n")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
```

## Eksperimen 3

| **Kondisi Deadlock** | **Terjadi di Versi Deadlock?**                                 | **Solusi di Versi Fixed**                                                                                                                                                                                                                                 |
| -------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mutual Exclusion** | Ya setiap garpu hanya bisa digunakan 1 filsuf                | Tetap ada (karena perlu), tetapi *akses garpu dikontrol* menggunakan **mutex atau semaphore** agar tidak menyebabkan hold-and-wait serentak                                                                                                               |
| **Hold and Wait**    | Ya  semua filsuf memegang garpu kiri dan menunggu garpu kanan | **Semaphore(1)**: filsuf hanya boleh mengambil kedua garpu sekaligus (menghilangkan hold-and-wait) <br> **Max 4**: tidak semua filsuf bisa menahan garpu kiri <br> **Odd-Even**: menghindari menunggu dalam kondisi simetris                              |
| **No Preemption**    | Ya  garpu tidak bisa direbut paksa                            | Tetap ada (karena garpu tidak bisa direbut), tetapi **deadlock hilang karena circular wait dihilangkan**                                                                                                                                                  |
| **Circular Wait**    | Ya  P0 menunggu P1 → P1 menunggu P2 → … → P4 menunggu P0      | **Max 4 philosophers**: siklus tidak bisa terbentuk <br> **Odd-Even Rule**: urutan pengambilan garpu diubah sehingga tidak ada lingkaran menunggu <br> **Semaphore mutex**: hanya satu yang boleh mengambil garpu, sehingga siklus tidak pernah terbentuk |


## Analisis


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## D. Tugas & Quiz
### Tugas
1. Analisis versi *Dining Philosophers* yang menyebabkan deadlock dan versi fixed yang bebas deadlock.  
2. Dokumentasikan hasil diskusi kelompok ke dalam `laporan.md`.  
3. Sertakan diagram atau screenshot hasil simulasi/pseudocode.  
4. Laporkan temuan penyebab deadlock dan solusi pencegahannya.  

### Quiz
Tuliskan jawaban di bagian **Quiz** laporan:
1. Sebutkan empat kondisi utama penyebab deadlock.  
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?  
3. Jelaskan perbedaan antara *semaphore* dan *monitor*.  

---

## E. Output yang Diharapkan
- Laporan analisis kelompok dalam `laporan.md`.  
- Screenshot hasil simulasi atau pseudocode disimpan di `screenshots/`.  
- Tabel analisis kondisi deadlock dan solusinya.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.  
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
