"""
Модуль для асинхронного завантаження контенту з веб-сторінок за допомогою aiohttp.
Містить функції для паралельного отримання контенту зі списку URL
з обробкою помилок підключення.
"""

import aiohttp
import asyncio
from typing import List


async def fetch_content(url: str) -> str:
    """
    Асинхронно отримує контент з веб-сторінки.

    Args:
        url (str): URL-адреса для запиту

    Returns:
        str: Контент сторінки або повідомлення про помилку
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                # Повертаємо контент навіть для HTTP статусів 4xx/5xx
                if response.status == 200:
                    return await response.text()
                else:
                    return f"⚠️ Помилка підключення до {url}: {response.status}: Не вдалося завантажити сторінку"

    except Exception as e:
        return f"⚠️ Невідома помилка для {url}: {str(e)}"


async def fetch_all(urls: List[str]) -> List[str]:
    """
    Паралельно завантажує контент зі списку URL.

    Args:
        urls (List[str]): Список URL-адрес

    Returns:
        List[str]: Список результатів (контент або помилки)
    """
    tasks = [asyncio.create_task(fetch_content(url)) for url in urls]

    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results


# Використання
async def main():
    urls = [
        "https://www.example.com",
        "https://www.google.com",
        "https://nonexistent.com",  # не існуючий URL
        "https://httpbin.org/status/500"  # Повертає помилки 500
    ]

    results = await fetch_all(urls)
    for i, content in enumerate(results):
        print(f"URL {i + 1}: {content[:250]}...")  # Вивід перших 250 символів вмісту повідомлення


if __name__ == "__main__":
    asyncio.run(main())
