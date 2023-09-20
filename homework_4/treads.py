import requests
import time
import threading
from urls import urls


def download(url, text="treads"):
    response = requests.get(url)
    filename = url.replace("https://", "").split("/")[-1]
    with open(f"homework_4/img/{text}-{filename}", "wb") as f:
        f.write(response.content)
        print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")


threads = []

start_time = time.time()

if __name__ == "__main__":
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
