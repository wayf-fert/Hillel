# Виконується послідовно, дуже повільний

import requests
import time


def sync_requests():
    url = "https://httpbin.org/get"
    for _ in range(500):
        requests.get(url)


start = time.time()
sync_requests()
print(f"Синхронно: {time.time() - start:.2f} сек")
