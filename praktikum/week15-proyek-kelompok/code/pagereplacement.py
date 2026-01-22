from tabulate import tabulate

def load_pages():
    with open("data/pages.txt") as f:
        return list(map(int, f.read().split()))

def fifo(pages, frames):
    memory = []
    faults = 0
    for p in pages:
        if p not in memory:
            faults += 1
            if len(memory) >= frames:
                memory.pop(0)
            memory.append(p)
    return faults

def lru(pages, frames):
    memory = []
    faults = 0
    for p in pages:
        if p not in memory:
            faults += 1
            if len(memory) >= frames:
                memory.pop(0)
        else:
            memory.remove(p)
        memory.append(p)
    return faults

def run_paging():
    pages = load_pages()
    frames = int(input("Jumlah frame: "))

    fifo_faults = fifo(pages, frames)
    lru_faults = lru(pages, frames)

    table = [
        ["FIFO", fifo_faults],
        ["LRU", lru_faults]
    ]

    print(tabulate(table, headers=["Algoritma", "Page Fault"]))
