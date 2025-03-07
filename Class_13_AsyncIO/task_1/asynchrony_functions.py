"""
Модуль для симуляції асинхронного завантаження веб-сторінок з використанням asyncio.

Паралельне "завантаження" сторінок з випадковими затримками.
"""

import asyncio
import random


async def download_page(url: str, semaphore) -> None:
    """
    Асинхронна функція для симуляції завантаження сторінки з обмеженням через semaphore.
    """
    async with semaphore:
        delay = random.uniform(1, 5)
        await asyncio.sleep(delay)
        print(f"Downloaded {url} in {delay:.2f} seconds")


async def main(urls: list[str], max_concurrent: int = 5) -> None:
    """
    Основна асинхронна функція для паралельного завантаження з обмеженням кількості одночасних запитів.

    Args:
        urls (list[str]): Список URL для завантаження
        max_concurrent (int): Максимальна кількість одночасних завантажень (за замовчуванням 5)
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    tasks = [asyncio.create_task(download_page(url, semaphore)) for url in urls]

    for task in asyncio.as_completed(tasks):
        await task  # Чекаємо завершення завдання


if __name__ == "__main__":
    sample_urls = [
                      "https://url_example.com",
                      "https://url_example.org",
                      "https://url_example.net",
                      "https://my_url.ua"
                  ] * 3
    asyncio.run(main(sample_urls, max_concurrent=5))
