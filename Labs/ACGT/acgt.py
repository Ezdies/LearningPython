import numpy as np
import time
from multiprocessing import Process, Array, cpu_count

def comparer(primer1, primer2):
    if not primer1 or not primer2:
        return -1
    else:
        primer2 = primer2[::-1]
        p1_tab = '*' * (len(primer1 + primer2) - 2) + primer1
        p2_tab = '*' * (len(primer1) - 1) + primer2
        align = []
        for i in range(len(primer1 + primer2) - 1):
            common = list(zip(p1_tab[i:], p2_tab))
            align.append(
                common.count(("A", "T")) + common.count(("T", "A")) +
                common.count(("C", "G")) + common.count(("G", "C"))
            )
        return max(align)

def main():
    file_in = open("primers.txt", "r")

    base = []
    print("Scanning...")
    for line in file_in:
        base.append(line.split(",")[0])
    count = len(base)
    print(count)
    cross = np.full((count, count), -1)
    THREAD_COUNT = cpu_count() + 1

    start_t = time.time()
    primer_1 = base[0]

    def calculate_thread(a, thread_index):
        start = int(thread_index * (count / THREAD_COUNT))
        end = int((thread_index + 1) * (count / THREAD_COUNT))

        # print(start, end)
        for i in range(start, end):
            primer_2 = base[i]
            a[i] = comparer(primer_1, primer_2)

    threads = []
    arr = Array('i', count)

    for i in range(THREAD_COUNT):
        thread = Process(target=calculate_thread, args=(arr,i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    s = sum(arr)

    end_t = time.time()
    print(0, "\t", end_t - start_t)
    print(s)
    print("Thread count:", THREAD_COUNT)

if __name__ == '__main__':
    main()