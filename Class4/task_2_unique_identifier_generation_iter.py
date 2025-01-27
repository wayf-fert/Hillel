import uuid


class UUIDGenerator:
    """Ітератор для генерації унікальних ідентифікаторів на основі UUID."""

    def __iter__(self):
        """Повертає ітератор."""
        return self

    def __next__(self):
        """Генерує наступний унікальний ідентифікатор."""
        return str(uuid.uuid4())


id_generator = UUIDGenerator()

for _ in range(3):
    print(next(id_generator))
