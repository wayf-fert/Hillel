"""
Асинхронний веб-сервер з двома маршрутами, реалізований за допомогою aiohttp.

Маршрути:
- /         : Миттєва відповідь з привітанням 'Hello, World!'
- /slow     : Спеціальний маршрут з штучною затримкою 5 секунд

Сервер здатний обробляти паралельні запити без блокування.
"""

from aiohttp import web
import asyncio


async def hello_processor(request: web.Request) -> web.Response:
    """
    Обробник для кореневого маршруту (/).

    Args:
        request (web.Request): Вхідний запит

    Returns:
        web.Response: Текстова відповідь "Hello, World!"
    """
    return web.Response(text="Hello, World!")


async def slow_processor(request: web.Request) -> web.Response:
    """
    Обробник для маршруту з штучною затримкою (/slow).

    Args:
        request (web.Request): Вхідний запит

    Returns:
        web.Response: Текстова відповідь після 5-секундної затримки
    """
    await asyncio.sleep(5)  # Імітація довгої операції
    return web.Response(text="Operation completed")


def create_app() -> web.Application:
    """
    Cтворення та налаштування веб-додатку.

    Returns:
        web.Application: Налаштований екземпляр додатку
    """
    app = web.Application()
    app.router.add_get('/', hello_processor)
    app.router.add_get('/slow', slow_processor)
    return app


def run_server():
    """
    Запускає веб-сервер на порту 8080.

    Конфігурує та запускає сервер з автоматичним вибором порту
    та обробником переривань.
    """
    web.run_app(
        create_app(),
        port=8080,
        print=lambda _: None  # Вимкнення стандартного виводу aiohttp
    )


if __name__ == '__main__':
    print("Сервер запущено на http://localhost:8080")
    print("Доступні маршрути:")
    print("  - GET http://localhost:8080/     : Швидкий запит")
    print("  - GET http://localhost:8080/slow : Повільний запит (5 сек)")
    run_server()
