import os
from typing import Iterator, Tuple


class IteratorDirectoryFiles:
    """
    Ітератор для проходження всіх файлів у заданому каталозі.

    Attributes:
        tree_of_files (str): Шлях до каталогу.
    """

    def __init__(self, tree_of_files: str) -> None:
        """
        Ініціалізує ітератор з указаним шляхом до каталогу.

        Args:
            tree_of_files (str): Шлях до каталогу.

        Raises:
            ValueError: Якщо вказаний шлях не є дійсним каталогом.
        """
        if not os.path.isdir(tree_of_files):
            raise ValueError(f"Шлях '{tree_of_files}' не є дійсним каталогом.")
        self.tree_of_files = tree_of_files
        self.files = (f for f in os.listdir(tree_of_files) if os.path.isfile(os.path.join(tree_of_files, f)))

    def __iter__(self) -> 'IteratorDirectoryFiles':
        """
        Returns:
            IteratorDirectoryFiles: Сам ітератор.
        """
        return self

    def __next__(self) -> Tuple[str, int]:
        """
        Повертає наступний файл у каталозі та його розмір.

        Returns:
            Tuple[str, int]: Назва файлу та його розмір у байтах.

        Raises:
            StopIteration: Якщо всі файли були оброблені.
        """
        file_name = next(self.files)  # Отримуємо наступний файл
        file_path = os.path.join(self.tree_of_files, file_name)
        file_size = os.path.getsize(file_path)
        return file_name, file_size


def print_directory_files(tree_of_files: str) -> None:
    """
    Проходить через файли в каталозі та виводить їхні назви та розміри.

    Args:
        tree_of_files (str): Шлях до каталогу.
    """
    try:
        iterator = IteratorDirectoryFiles(tree_of_files)
        for file_name, file_size in iterator:
            print(f"Назва: {file_name}, Розмір: {file_size} байтів")
    except ValueError as e:
        print(e)


directory_path = input("Введіть шлях до каталогу: ")  # Запит шляху до каталогу

with open(directory_path, "w", encoding='utf-8') as f:
    f.write("2024-10-27 10:00:00 - INFO - Request received\n")
    f.write("2024-10-27 10:00:01 - ERROR - 404 Not Found\n")
    f.write("2024-10-27 10:00:02 - INFO - Processing request\n")
    f.write("2024-10-27 10:00:03 - ERROR - 500 Internal Server Error\n")
    f.write("2024-10-27 10:00:04 - WARNING - 403 Forbidden\n")
    f.write("2024-10-27 10:00:05 - INFO - Request completed\n")
    f.write("2024-10-27 10:00:06 - ERROR - 503 Service Unavailable\n")

print_directory_files(directory_path)
