from scheduling import run_scheduling
from pagereplacement import run_paging
from deadlock import run_deadlock_detection

def menu():
    while True:
        print("\n=== MINI SIMULASI SISTEM OPERASI ===")
        print("1. CPU Scheduling (FCFS & SJF)")
        print("2. Page Replacement (FIFO & LRU)")
        print("3. Deadlock Detection")
        print("0. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            run_scheduling()
        elif choice == "2":
            run_paging()
        elif choice == "3":
            run_deadlock_detection()
        elif choice == "0":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
