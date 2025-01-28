import os


class ReverseFileReader:
    """
    Ітератор зворотного читання файлу рядок за рядком з кінця файлу до початку.

    Attributes:
        file_path (str): Шлях до файлу.
        lines (list[str]): Містить рядки файлу у зворотному порядку.
        index (int): Поточний індекс для ітерації.
    """

    def __init__(self, file_path: str) -> None:
        """
        Ініціалізує ітератор з указаним шляхом до файлу.

        Args:
            file_path (str): Шлях до файлу.

        Raises:
            FileNotFoundError: Якщо файл не знайдено.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл '{file_path}' не знайдено. Перевірте шлях до файлу.")

        self.file_path = file_path
        with open(file_path, 'r') as file:
            self.lines = file.readlines()
        self.lines.reverse()
        self.index = 0

    def __iter__(self) -> 'ReverseFileReader':

        return self

    def __next__(self) -> str:
        """
        Повертає наступний рядок у зворотному порядку.

        Returns:
            str: Рядок тексту з файлу.

        Raises:
            StopIteration: Якщо досягнуто початок файлу.
        """
        if self.index >= len(self.lines):
            raise StopIteration

        line = self.lines[self.index]
        self.index += 1
        return line


filepath = 'task_1_Test.log'

if not os.path.exists(filepath):
    raise FileNotFoundError(f"Файл '{filepath}' не знайдено. Перевірте шлях до файлу.")

reverse_iterator = ReverseFileReader(filepath)

for line in reverse_iterator:
    print(line.strip())
