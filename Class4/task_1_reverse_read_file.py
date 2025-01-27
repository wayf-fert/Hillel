class ReverseFileReader:
    """
    Ітератор для зворотного читання файлу рядок за рядком з кінця файлу до початку.

    Attributes:
        file_path (str): Шлях до файлу.
        file (file): Об'єкт файлу для читання.
        lines (list[str]): Містить рядки файлу у зворотному порядку.
        index (int): Поточний індекс для ітерації.
    """

    def __init__(self, file_path: str) -> None:
        """
        Ініціалізує ітератор з указаним шляхом до файлу.

        Args:
            file_path (str): Шлях до файлу.
        """
        self.file_path = file_path
        with open(file_path, 'r') as file:
            self.lines = file.readlines()
        self.lines.reverse()  # Обертання списку рядків
        self.index = 0

    def __iter__(self) -> 'ReverseFileReader':
        """
        Повертає сам ітератор.

        Returns:
            ReverseFileReader: Сам ітератор.
        """
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

reverse_iterator = ReverseFileReader(filepath)

for line in reverse_iterator:
    print(line.strip())

if open(filename, 'rb'):
    for line in ReverseFileReader(filename):
        print(line)
else:
    print(f"Файл '{filename}' не знайдено. Перевірте шлях до файлу.")
