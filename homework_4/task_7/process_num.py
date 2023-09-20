from multiprocessing import Process
import multiprocessing
import time
from treads_num import LENGTH, MIN, MAX, CUT, get_random_array, cut_array


def sum_number(array, summa, timer):
    with summa.get_lock():
        summa.value += sum(array)
        t = time.time() - start_time
        timer.value += t
    print(f"Sum numbers in {summa.value:_} counted in {timer.value:.2f} seconds")


summa = multiprocessing.Value("i", 0)
timer = multiprocessing.Value("f", 0.0)

array = get_random_array(LENGTH, MIN, MAX)
start_time = time.time()

processes = []

if __name__ == "__main__":
    for i in cut_array(array, CUT):
        process = Process(
            target=sum_number,
            args=(i, summa, timer),
        )
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
