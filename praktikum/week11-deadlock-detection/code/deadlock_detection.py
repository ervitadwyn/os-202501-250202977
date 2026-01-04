import csv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "dataset_deadlock.csv")

processes = []
allocation = {}
request = {}

with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Process"]
        processes.append(p)
        allocation[p] = row["Allocation"]
        request[p] = row["Request"]

finished = {}
for p in processes:
    finished[p] = False

available = set()

progress = True
while progress:
    progress = False
    for p in processes:
        if not finished[p]:
            if request[p] in available:
                finished[p] = True
                available.add(allocation[p])
                progress = True

deadlock = []
for p in processes:
    if not finished[p]:
        deadlock.append(p)

print("HASIL DETEKSI DEADLOCK")
if deadlock:
    print("Deadlock terdeteksi!")
    print("Proses yang terlibat deadlock:")
    for p in deadlock:
        print("-", p)
else:
    print("Tidak terjadi deadlock.")
