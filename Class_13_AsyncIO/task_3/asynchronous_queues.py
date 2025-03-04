"""
Асинхронна система черги завдань з використанням asyncio.Queue.
Містить механізми для паралельного додавання та обробки завдань з різною швидкістю.
"""

import asyncio


async def producer(queue: asyncio.Queue, num_consumers: int) -> None:
    """
    Виробник завдань: додає 5 елементів у чергу з інтервалом 1 секунда.

    Args:
        queue (asyncio.Queue): Черга для обміну даними
        num_consumers (int): Кількість споживачів для сигналів завершення
    """
    for i in range(5):
        await asyncio.sleep(1)
        task = f"Завдання {i + 1}"
        await queue.put(task)
        print(f"[Producer] ➕ Додано: {task}")

    for _ in range(num_consumers):
        await queue.put(None)
    print("[Producer] 🏁 Завершив роботу")


async def consumer(queue: asyncio.Queue, consumer_id: int) -> None:
    """
    Споживач завдань: обробляє елементи з черги з інтервалом 2 секунди.

    Args:
        queue (asyncio.Queue): Черга для обміну даними
        consumer_id (int): Унікальний ідентифікатор споживача
    """
    while True:
        task = await queue.get()
        if task is None:
            queue.task_done()
            print(f"[Consumer #{consumer_id}] 🛑 Зупинка")
            break

        print(f"\n[Consumer #{consumer_id}] ⚠️ Початок: {task}")
        await asyncio.sleep(2)  # Імітація тривалої роботи
        print(f"[Consumer #{consumer_id}] ✅ Завершено: {task}")
        queue.task_done()


async def main() -> None:
    queue = asyncio.Queue(maxsize=5)  # Обмеження черги
    consumers_count = 3

    await asyncio.gather(
        producer(queue, consumers_count),
        *(consumer(queue, i + 1) for i in range(consumers_count))
    )
    print("\n[System]: 🛑 Всі завдання оброблено")


if __name__ == "__main__":
    asyncio.run(main())
