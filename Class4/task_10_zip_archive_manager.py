import os


class ReverseFileReader:
    """Ітератор для зворотного читання файлу рядок за рядком з кінця файлу до початку.

    Attributes:
        file_path (str): Шлях до файлу.
        lines (list[str]): Список рядків файлу у зворотному порядку.
        index (int): Поточний індекс для ітерації.
    """

    def __init__(self, file_path: str) -> None:
        """Ініціалізує ітератор з указаним шляхом до файлу.

        Args:
            file_path (str): Шлях до файлу.

        Raises:
            ValueError: Якщо файл за вказаним шляхом не існує.
        """
        if not os.path.exists(file_path):
            raise ValueError(f"Файл '{file_path}' не знайдено. Перевірте шлях до файлу.")

        self.file_path = file_path
        with open(file_path, 'r') as file:
            self.lines = file.readlines()

        self.lines.reverse()
        self.index = 0

    def __iter__(self) -> 'ReverseFileReader':
        return self

    def __next__(self) -> str:
        if self.index >= len(self.lines):
            raise StopIteration

        line = self.lines[self.index]
        self.index += 1
        return line


filename = 'task_10_Test.txt'

if os.path.exists(filename):
    print(f"Читання файлу '{filename}' у зворотному порядку:")
    reverse_reader = ReverseFileReader(filename)
    for line in reverse_reader:
        print(line.strip())
else:
    print(f"Файл '{filename}' не знайдено. Перевірте шлях до файлу.")
