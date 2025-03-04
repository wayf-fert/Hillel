"""
Модуль для симуляції асинхронного завантаження веб-сторінок з використанням asyncio.

Паралельне "завантаження" сторінок з випадковими затримками.
"""

import asyncio
import random


async def download_page(url: str) -> None:
    """
    Асинхронна функція для симуляції завантаження сторінки від 1 - 5 секунд
    """
    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)
    print(f"Downloaded {url} in {delay:.2f} seconds")


async def main(urls: list[str]) -> None:
    """
    Основна асинхронна функція для паралельного завантаження списку URL.

    Args:
        urls (list[str]): Список URL для завантаження
    """
    await asyncio.gather(*(download_page(url) for url in urls))


if __name__ == "__main__":
    # Використання
    sample_urls = [
        "https://url_example.com",
        "https://url_example.org",
        "https://url_example.net",
        "https://my_url.ua"
    ]
    asyncio.run(main(sample_urls))
