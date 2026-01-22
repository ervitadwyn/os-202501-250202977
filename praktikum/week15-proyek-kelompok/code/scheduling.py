import csv
from tabulate import tabulate

def load_data():
    processes = []
    with open("data/scheduling.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            processes.append({
                "pid": row["PID"],
                "arrival": int(row["Arrival"]),
                "burst": int(row["Burst"])
            })
    return processes

def fcfs(processes):
    time = 0
    result = []
    for p in sorted(processes, key=lambda x: x["arrival"]):
        start = max(time, p["arrival"])
        wait = start - p["arrival"]
        turnaround = wait + p["burst"]
        time = start + p["burst"]
        result.append([p["pid"], wait, turnaround])
    return result

def sjf(processes):
    time = 0
    completed = []
    ready = processes[:]
    result = []

    while ready:
        available = [p for p in ready if p["arrival"] <= time]
        if not available:
            time += 1
            continue
        p = min(available, key=lambda x: x["burst"])
        ready.remove(p)
        wait = time - p["arrival"]
        turnaround = wait + p["burst"]
        time += p["burst"]
        result.append([p["pid"], wait, turnaround])
    return result

def run_scheduling():
    processes = load_data()
    print("\n--- FCFS ---")
    fcfs_res = fcfs(processes)
    print(tabulate(fcfs_res, headers=["PID", "Waiting", "Turnaround"]))

    print("\n--- SJF ---")
    sjf_res = sjf(processes)
    print(tabulate(sjf_res, headers=["PID", "Waiting", "Turnaround"]))
