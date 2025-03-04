"""
Асинхронний веб-скрапер для паралельного завантаження зображень з використанням aiohttp.
"""

import aiohttp
import asyncio
import os
from typing import List, Tuple


async def download_image(url: str, filename: str) -> None:
    """
    Асинхронно завантажує та зберігає зображення з вказаного URL.

    Args:
        url (str): URL-адреса зображення
        filename (str): Імʼя для збереження файлу
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()

                    # Створюємо директорію, якщо не існує
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    with open(filename, 'wb') as f:
                        f.write(content)
                    print(f"✅ Успішно збережено: {filename}")
                else:
                    print(f"⚠️ Помилка {response.status} для {url}")

    except aiohttp.ClientError as e:
        print(f"⚠️ Помилка підключення: {url} - {str(e)}")
    except Exception as e:
        print(f"🛑 Невідома помилка: {filename} - {str(e)}")


async def main(image_list: List[Tuple[str, str]]) -> None:
    """
    Основна функція для паралельного завантаження зображень.

    Args:
        image_list (List[Tuple[str, str]]): Список кортежів (URL, filename)
    """
    tasks = [
        download_image(url, filename)
        for url, filename in image_list
    ]

    await asyncio.gather(*tasks)
    print("\n🏁 Всі завдання завершено!")


if __name__ == "__main__":
    # Приклад використання
    images_to_download = [
        ("https://example.com/image1.jpg", "downloads/img1.jpg"),
        ("https://example.com/image2.png", "downloads/img2.png"),
        ("https://invalid.url/invalid_image.jpg", "downloads/error.jpg")
    ]

    # Асинхронне виконання
    asyncio.run(main(images_to_download))
