# Використовує потоки, прискорює мережеві запити

import requests
import time
from concurrent.futures import ThreadPoolExecutor


def thread_requests():
    url = "https://httpbin.org/get"
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda _: requests.get(url), range(500))


start = time.time()
thread_requests()
print(f"Потоки: {time.time() - start:.2f} сек")
