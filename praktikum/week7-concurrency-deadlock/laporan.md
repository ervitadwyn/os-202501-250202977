
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
![Screenshot hasil](screenshots/Simulasidiningphilosophers.png)
![Screenshot hasil](screenshots/Simulasifixedversionsemaphore(mutexglobal).png)
![Screenshot hasil](screenshots/Simulasifixedversionbatas4maxfilsuf.png)
![Screenshot hasil](screenshots/Simulasifixedversionoddevenforkpickingrule.png)

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

## Eksperimen 1

Deadlock terjadi ketika seluruh filsuf telah mengambil garpu kiri dan secara bersamaan menunggu garpu kanan. Setiap garpu kanan sedang dipegang oleh filsuf lain sehingga membentuk lingkaran tunggu (circular wait). Akibatnya tidak ada thread yang dapat melanjutkan eksekusi dan program berhenti pada kondisi menunggu selamanya.
Penjelasan :
1. Semua filsuf mulai think()
2. Semua filsuf mencoba mengambil garpu kiri → berhasil
3. Semua filsuf mencoba mengambil garpu kanan → semua terblokir
4. Tidak ada filsuf yang dapat makan → deadlock total
---

## Eksperimen 2

1) Solusi A Semaphore (mutex global)

Perubahan: sebelum mengambil garpu, setiap filsuf harus wait(mutex) (semaphore(1)) sehingga hanya 1 filsuf yang boleh masuk ke tahap mengambil kedua garpu sekaligus. Setelah kedua garpu diambil, signal(mutex).

Mengapa deadlock dihilangkan :

Untuk deadlock klasik, keempat kondisi Coffman harus terpenuhi. Teknik ini menghilangkan kondisi Hold-and-Wait: karena filsuf tidak lagi diperbolehkan memegang satu garpu sambil menunggu garpu lain. Ia hanya boleh masuk ke critical section apabila bisa langsung mengambil kedua garpu (karena mutex mem-serial-kan pengambilan).

Tanpa hold-and-wait, tidak mungkin semua filsuf menahan satu garpu dan menunggu lainnya → tidak ada siklus menunggu lengkap.

Bukti informal formal:

Misal ada N filsuf. Karena mutex=1, pada waktu tertentu paling banyak 1 filsuf yang sedang melakukan operasi:

acquire(mutex)
acquire(left)
acquire(right)
release(mutex)


Selama filsuf A di critical section, B tidak dapat memulai sequence acquire(left) maka B tidak akan menahan garpu kiri bersamaan dengan A. Jadi tidak ada konfigurasi di mana setiap filsuf memegang satu garpu dan menunggu yang lain.

Cara verifikasi di program :

Saat dijalankan, kamu akan melihat pola: beberapa filsuf berpikir, lalu satu filsuf mengambil kedua garpu dan makan, lalu melepaskan; lalu filsuf lain mendapat giliran.

Indikator tidak-deadlock: dalam window waktu > beberapa detik akan selalu ada progress (setidaknya satu sedang makan... muncul periodik).

2) Solusi B Pembatasan ruang: room semaphore (max 4)

Perubahan: sebelum mencoba mengambil garpu, filsuf wait(room) pada semaphore 4. Hanya 4 filsuf yang boleh masuk mencoba mengambil garpu; minimal 1 filsuf tetap di luar.

Mengapa deadlock dihilangkan :

Deadlock memerlukan setiap filsuf menahan garpu kiri lalu menunggu garpu kanan untuk membentuk siklus panjang (5 → 5). Jika paling banyak 4 yang mencoba, minimal satu garpu akan tetap bebas sehingga setidaknya satu filsuf bisa mengambil kedua garpu dan makan.

Dengan kemunculan satu filsuf yang tidak ikut berebut, siklus P0→P1→...→P4 tidak dapat terbentuk.

Bukti informal :

Asumsikan N=5. Jika hanya k=4 filsuf yang berada dalam fase "mengambil garpu", maka setidaknya 1 garpu tidak dipegang oleh siapapun. Karena setiap filsuf membutuhkan 2 garpu yang bersebelahan, ada setidaknya satu pasangan garpu kosong/tersedia sehingga ada filsuf yang bisa mendapatkan kedua garpu → ia makan → melepaskan → memberi jalan bagi yang lain. Maka tidak mungkin stuck dalam keadaan di mana semua menunggu.

Cara verifikasi di program

Saat dijalankan: kamu akan lihat paling banyak 4 filsuf mencetak mencoba mengambil garpu kiri ... bersamaan; namun selalu ada Filsuf X sedang makan... yang muncul secara berkala.

Gunakan deteksi: jika tidak ada output sedang makan selama X detik (X besar), maka ada masalah — tapi pada implementasi ini seharusnya tidak terjadi.

3) Solusi C  Odd–Even Fork Picking Rule

Perubahan: filsuf dengan id genap mengambil left dulu lalu right; filsuf ganjil mengambil right dulu lalu left.

Mengapa deadlock dihilangkan :

Circular wait bergantung pada urutan pengambilan sumber daya yang sama untuk semua proses. Dengan membuat urutan berbeda antar proses (paritas), tidak mungkin muncul siklus lengkap.

Secara formal, atur tiap garpu diberi nomor; setiap filsuf meminta dua garpu dengan urutan yang menjamin adanya partial order pada permintaan; karena ada setidaknya satu edge arah terbalik dalam siklus, siklus tidak konsisten → kontradiksi.

Bukti formal singkat :

Misal P_i meminta sumber A kemudian B, dan P_j meminta B kemudian A. Untuk membentuk siklus menunggu yang mengitari semua filsuf, setiap edge “menunggu” harus konsisten dengan arah permintaan. Tetapi jika ada pasangan berurutan (even/odd) yang meminta terbalik, maka satu hubungan memecah kemungkinan siklus penuh. Oleh karena itu circular wait tidak dapat terjadi.

Cara verifikasi di program :

Jalankan versi odd-even; cek log: beberapa filsuf bisa mengambil dan makan bersamaan (paralelisme tinggi). Kamu tidak akan melihat pola “semua mengambil left saja lalu menunggu right” lagi.

Perhatikan adanya interleaving di mana beberapa filsuf sukses mengambil kedua garpu walau tetangganya memegang satu.

## Kesimpulan

1. Versi awal (deadlock version) membuktikan bahwa tanpa mekanisme kontrol, seluruh filsuf dapat masuk kondisi deadlock.

Deadlock terjadi ketika setiap filsuf berhasil mengambil satu garpu (kiri) namun semua menunggu garpu kanan yang dipegang tetangganya. Hal ini memenuhi empat kondisi deadlock (mutual exclusion, hold-and-wait, no preemption, dan circular wait), sehingga tidak ada proses yang dapat melanjutkan eksekusi.

2. Modifikasi pada versi fixed berhasil menghilangkan minimal satu kondisi deadlock, sehingga sistem selalu tetap bergerak (making progress).

Baik dengan semaphore global, pembatasan jumlah filsuf (max 4), maupun aturan pengambilan garpu ganjil–genap, sistem tidak lagi dapat membentuk circular wait atau hold-and-wait. Hasil simulasi menunjukkan bahwa selalu ada filsuf yang dapat makan secara periodik, yang menandakan deadlock berhasil dicegah.

3. Setiap strategi pencegahan deadlock memiliki kelebihan dan kelemahan, namun semua terbukti efektif menghindari kebuntuan total.

Semaphore global memberikan kepastian aman tapi mengurangi paralelisme, pembatasan kapasitas (max 4) lebih efisien, sedangkan strategi ganjil–genap memberikan performa terbaik karena mempertahankan paralelisme sekaligus memutus siklus menunggu.

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
   **Jawaban:**
   
   Empat kondisi utama (syarat) terjadinya *deadlock* menurut teori klasikal (Coffman conditions) adalah:

    -Mutual Exclusion :
   
   Setiap resource hanya dapat digunakan oleh satu proses pada satu waktu.

   -Hold and Wait :
   
   Proses sudah memegang satu resource dan menunggu resource lain yang sedang dipegang proses lain.

   -No Preemption :
   
   Resource yang sedang digunakan proses tidak dapat diambil paksa; hanya dapat dilepaskan secara sukarela oleh proses tersebut.

   -Circular Wait :
   
   Terjadi rantai proses yang saling menunggu, misalnya P1 menunggu resource yang dipegang P2, P2 menunggu resource yang dipegang P3, dan seterusnya hingga kembali ke P1.


3. Mengapa sinkronisasi diperlukan dalam sistem operasi?  
   **Jawaban:**
   
Sinkronisasi diperlukan dalam sistem operasi untuk memastikan bahwa proses atau thread yang berjalan secara bersamaan dapat mengakses resource bersama dengan aman. Tanpa sinkronisasi, kondisi seperti *race condition* dapat terjadi ketika beberapa proses mengubah data secara bersamaan sehingga menghasilkan output yang tidak dapat diprediksi. Mekanisme sinkronisasi juga menjaga konsistensi dan integritas data, mencegah terjadinya kerusakan atau ketidaksesuaian akibat akses yang tak terkoordinasi. Selain itu, sinkronisasi memungkinkan koordinasi eksekusi antar-proses, memastikan bahwa proses tertentu berjalan dalam urutan yang benar sesuai kebutuhan. Dengan penerapan sinkronisasi yang baik, sistem dapat terhindar dari *deadlock* serta memanfaatkan resource secara lebih optimal dan efisien.


3. Jelaskan perbedaan antara *semaphore* dan *monitor*
   **Jawaban:**  

Semaphore adalah struktur sinkronisasi berbasis variabel counter yang dapat memiliki nilai integer, dan penggunaannya bergantung pada operasi dasar wait (P) dan signal (V). Semaphore bersifat *low-level*, sehingga programmer harus mengatur sendiri kapan harus memanggil wait atau signal. Hal ini membuat semaphore fleksibel tetapi rawan kesalahan seperti *deadlock* atau *missed wakeup* jika urutan pemanggilan tidak tepat. Semaphore juga tidak memiliki batasan bahwa operasi harus terikat pada satu blok kode tertentu.

sebaliknya, Monitor adalah mekanisme sinkronisasi *high-level* yang menggabungkan data, operasi, dan pengendalian akses dalam satu abstraksi. Monitor memastikan bahwa hanya satu thread yang dapat mengeksekusi fungsi di dalamnya pada satu waktu, sehingga memberikan *mutual exclusion* secara otomatis. Selain itu, monitor biasanya menggunakan *condition variable* untuk mengatur thread yang harus menunggu dan bangun pada keadaan tertentu. Karena sifatnya yang terstruktur, monitor lebih aman dan mudah digunakan dibanding semaphore, tetapi fleksibilitasnya lebih rendah.


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
