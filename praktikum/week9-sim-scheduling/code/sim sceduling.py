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
