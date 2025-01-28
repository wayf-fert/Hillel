import os
from typing import Iterator, Tuple


class IteratorDirectoryFiles:
    """
    Ітератор для проходження всіх файлів у заданому каталозі.

    Attributes:
        directory (str): Шлях до каталогу.
    """

    def __init__(self, directory: str) -> None:
        """
        Ініціалізує ітератор з указаним шляхом до каталогу.

        Args:
            directory (str): Шлях до каталогу.

        Raises:
            ValueError: Якщо вказаний шлях не є дійсним каталогом.
        """
        if not os.path.isdir(directory):
            raise ValueError(f"Шлях '{directory}' не є дійсним каталогом.")
        self.directory = directory
        self._files = iter([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

    def __iter__(self) -> Iterator[Tuple[str, int]]:
        """
        Повертає себе як об'єкт ітератора.
        """
        return self

    def __next__(self) -> Tuple[str, int]:
        """
        Повертає наступний файл у каталозі та його розмір.

        Returns:
            Tuple[str, int]: Назва файлу та його розмір у байтах.

        Raises:
            StopIteration: Коли всі файли вже були оброблені.
        """
        file_name = next(self._files)
        file_path = os.path.join(self.directory, file_name)
        file_size = os.path.getsize(file_path)
        return file_name, file_size


def print_directory_files(directory: str) -> None:
    """
    Виводить назви та розміри всіх файлів у вказаному каталозі.

    Args:
        directory (str): Шлях до каталогу.
    """
    try:
        for file_name, file_size in IteratorDirectoryFiles(directory):
            print(f"Назва: {file_name}, Розмір: {file_size} байтів")
    except ValueError as e:
        print(e)


directory_path = input("Введіть шлях до каталогу: ")
print_directory_files(directory_path)
