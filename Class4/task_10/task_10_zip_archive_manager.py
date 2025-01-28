import os
import zipfile
from typing import List


class ZipArchiveManager:
    """
    Менеджер контексту для архівування файлів за допомогою модуля zipfile.

    Attributes:
        archive_path (str): Шлях до архіву.
        files_to_archive (List[str]): Список файлів для архівування.
    """

    def __init__(self, archive_path: str, files_to_archive: List[str]) -> None:
        """
        Ініціалізує менеджер контексту для архівування файлів.

        Args:
            archive_path (str): Шлях до архіву.
            files_to_archive (List[str]): Список файлів для архівування.
        """
        self.archive_path = archive_path
        self.files_to_archive = files_to_archive

    def __enter__(self) -> 'ZipArchiveManager':
        """
        Відкриває архів для запису файлів.

        Returns:
            ZipArchiveManager: Сам менеджер контексту.
        """
        self.archive = zipfile.ZipFile(self.archive_path, 'w', zipfile.ZIP_DEFLATED)
        return self

    def add_files(self) -> None:
        """
        Додає файли до архіву.
        """
        for file_path in self.files_to_archive:
            if os.path.exists(file_path):
                self.archive.write(file_path, os.path.basename(file_path))
                print(f"Файл '{file_path}' додано до архіву.")
            else:
                print(f"Файл '{file_path}' не знайдено. Пропущено.")

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Завершує архівування та закриває архів.

        Args:
            exc_type: Тип виключення, якщо виникло.
            exc_val: Значення виключення, якщо виникло.
            exc_tb: Трасування виключення, якщо виникло.
        """
        self.archive.close()
        print(f"Архів '{self.archive_path}' успішно створено")


# Приклад використання
files_to_archive = ['/Users/pavel/EDU/Hillel/Class4/task_9/task_9_backup.py', 'my_folder', 'Skip_File.log']
archive_path = 'task_10_My_archive.zip'  # Шлях до архіву

with ZipArchiveManager(archive_path, files_to_archive) as archive_manager:
    archive_manager.add_files()