from multiprocessing import Process
import time
from urls import urls
from treads import download


processes = []

start_time = time.time()

if __name__ == "__main__":
    for url in urls:
        process = Process(target=download, args=(url, "process"))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
