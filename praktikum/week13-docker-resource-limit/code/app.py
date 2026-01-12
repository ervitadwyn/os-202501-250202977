import time
import sys

data = []
print("Program dimulai...")
sys.stdout.flush()

try:
    i = 0
    while True:
        for _ in range(5_000_000):
            pass

        data.append("X" * 5_000_000)  # ±5 MB
        i += 1
        print(f"Iterasi ke-{i}, alokasi memori bertambah")
        sys.stdout.flush()
        time.sleep(1)

except MemoryError:
    print("MemoryError: Memori tidak cukup!")
