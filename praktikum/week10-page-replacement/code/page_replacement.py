def fifo_page_replacement(reference_string, frame_count):
    frames = []
    page_faults = 0
    index = 0

    print("=== FIFO Page Replacement ===")
    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[index] = page
                index = (index + 1) % frame_count
            status = "Fault"
        else:
            status = "Hit"

        print(f"Page: {page} -> Frames: {frames} ({status})")

    return page_faults


def lru_page_replacement(reference_string, frame_count):
    frames = []
    recent = {}
    page_faults = 0
    time = 0

    print("\n=== LRU Page Replacement ===")
    for page in reference_string:
        time += 1
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                lru_page = min(recent, key=recent.get)
                frames[frames.index(lru_page)] = page
                del recent[lru_page]
            status = "Fault"
        else:
            status = "Hit"

        recent[page] = time
        print(f"Page: {page} -> Frames: {frames} ({status})")

    return page_faults


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 3

fifo_faults = fifo_page_replacement(reference_string, frame_count)
lru_faults = lru_page_replacement(reference_string, frame_count)

print("\n=== HASIL AKHIR ===")
print(f"Total Page Fault FIFO: {fifo_faults}")
print(f"Total Page Fault LRU : {lru_faults}")
