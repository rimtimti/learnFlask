import random
import threading
import time

LENGTH = 1_000_000
MIN = 1
MAX = 100
CUT = 100_000


def get_random_array(length, min_number, max_number):
    return [random.randint(min_number, max_number) for _ in range(length)]


def sum_number(array):
    global summa
    summa += sum(array)
    print(f"Sum numbers = {summa} counted in {time.time() - start_time:.2f} seconds")


def cut_array(array, n):
    for i in range(0, len(array), n):
        yield array[i : i + n]


summa = 0

array = get_random_array(LENGTH, MIN, MAX)
start_time = time.time()

threads = []

if __name__ == "__main__":
    for i in cut_array(array, CUT):
        thread = threading.Thread(target=sum_number, args=[i])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
