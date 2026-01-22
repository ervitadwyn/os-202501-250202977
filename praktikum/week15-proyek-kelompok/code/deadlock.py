from tabulate import tabulate

def run_deadlock_detection():
    allocation = [
        [0,1,0],
        [2,0,0],
        [3,0,3],
        [2,1,1],
        [0,0,2]
    ]

    request = [
        [0,0,0],
        [2,0,2],
        [0,0,0],
        [1,0,0],
        [0,0,2]
    ]

    available = [0,0,0]

    n = len(allocation)
    finished = [False] * n
    work = available[:]

    changed = True
    while changed:
        changed = False
        for i in range(n):
            if not finished[i]:
                if all(request[i][j] <= work[j] for j in range(len(work))):
                    for j in range(len(work)):
                        work[j] += allocation[i][j]
                    finished[i] = True
                    changed = True

    deadlocked = [f"P{i}" for i in range(n) if not finished[i]]

    print("\n=== DEADLOCK DETECTION ===")
    if deadlocked:
        print("STATUS : DEADLOCK TERDETEKSI ")
        print("Proses yang terlibat:")
        print(tabulate([[p] for p in deadlocked], headers=["Process"]))
    else:
        print("STATUS : TIDAK ADA DEADLOCK")
