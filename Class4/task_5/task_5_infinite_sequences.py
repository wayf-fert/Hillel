class InfiniteSequenceGenerator:
    """Менеджер контексту для обмеження кількості збережених чисел у файл.

    Args:
        filename (str): Ім'я файлу для запису.
        limit (int): Максимальна кількість чисел для запису.
        count (int): Лічильник записаних чисел.
    """

    def __init__(self, filename: str, limit: int):
        self.filename = filename
        self.limit = limit
        self.count = 0

    def __enter__(self) -> "InfiniteSequenceGenerator":
        self.file = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закриває файл після завершення роботи."""
        self.file.close()

    def write_numbers(self, generator) -> None:
        """Записує числа з генератора у файл до досягнення ліміту.

        Args:
            generator: Генератор чисел.
        """
        for number in generator:
            if self.count >= self.limit:
                break
            self.file.write(f"{number}\n")
            self.count += 1


def even_number_generator():
    """Генератор, що генерує нескінченну послідовність парних чисел."""
    n = 0
    while True:
        yield n
        n += 2


generator = even_number_generator()

with InfiniteSequenceGenerator("task_5_even_numbers.txt", 100) as writer:
    writer.write_numbers(generator)

with open("task_5_even_numbers.txt", "r") as file:
    content = file.read()
    print(content)
