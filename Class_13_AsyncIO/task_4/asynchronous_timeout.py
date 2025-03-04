import asyncio


async def slow_task():
    """
    Імітує довготривале завдання з затримкою 10 секунд.

    Виводить повідомлення про початок та успішне завершення.
    """
    print(" Завдання розпочато...")
    try:
        await asyncio.sleep(10)  # Імітація 10-секундної роботи
        print("✅ Завдання успішно завершено!")
    except asyncio.CancelledError:
        print("🛑 Завдання перервано через тайм-аут!")
        raise


async def main():
    """
    Виконує slow_task() з обмеженням часу 5 секунд.
    Обробляє перевищення часу та інші помилки.
    """
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("⚠️ Помилка: перевищено час очікування (5 секунд)!")


if __name__ == "__main__":
    asyncio.run(main())
