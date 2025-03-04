# Використовує окремі процеси, але HTTP-запити не ефективні для CPU-bound

from concurrent.futures import ProcessPoolExecutor
import requests
import time


def fetch_url(_):
    url = "https://httpbin.org/get"
    return requests.get(url)


def process_requests():
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(fetch_url, range(500))


if __name__ == '__main__':
    start = time.time()
    process_requests()
    print(f"Процеси: {time.time() - start:.2f} сек")
