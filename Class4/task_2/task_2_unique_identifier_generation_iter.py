import uuid


class UUIDGenerator:
    """
    Ітератор для генерації унікальних ідентифікаторів на основі UUID.

    Attributes:
        limit (int): Максимальна кількість ідентифікаторів для генерації. Якщо None, ітератор безмежний.
        count (int): Лічильник згенерованих ідентифікаторів.
    """

    def __init__(self, limit: int = None):
        """
        Ініціалізує ітератор з вказаною максимальною кількістю ідентифікаторів.

        Args:
            limit (int, optional): Максимальна кількість ідентифікаторів. За замовчуванням None (безмежно).
        """
        self.limit = limit
        self.count = 0

    def __iter__(self):
        """Повертає ітератор."""
        return self

    def __next__(self):
        """
        Генерує наступний унікальний ідентифікатор.

        Returns:
            str: Унікальний ідентифікатор (UUID).

        Raises:
            StopIteration: Якщо досягнуто ліміт генерації.
        """
        if self.limit is not None and self.count >= self.limit:
            raise StopIteration

        self.count += 1
        return str(uuid.uuid4())


# Приклад використання
id_generator = UUIDGenerator(limit=5)  # Обмеження на 5 ідентифікаторів

for unique_id in id_generator:
    print(unique_id)
