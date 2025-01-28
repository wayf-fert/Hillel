import os
import csv
from PIL import Image


class MetadataImagesCollector:
    """Клас для збору метаданих зображень у каталозі.

    Args:
        directory (str): Каталог, у якому знаходяться зображення.
        csv_file (str): Ім'я CSV-файлу для збереження метаданих.
        image_files (list[str]): Список файлів зображень у каталозі.
    """

    def __init__(self, directory: str, csv_file: str = "task_3_image_metadata.csv") -> None:
        """Ініціалізує об'єкт MetadataImagesCollector."""
        self.directory = directory
        self.csv_file = csv_file
        self.image_files = [f for f in os.listdir(directory) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

    def __iter__(self):
        """Ініціалізує ітератор."""
        self.index = 0
        return self

    def __next__(self) -> dict:
        """Повертає наступний елемент ітератора.

        Return:
            dict: Метадані для поточного зображення.
        """
        if self.index >= len(self.image_files):
            raise StopIteration

        some_file = self.image_files[self.index]
        self.index += 1

        filepath = os.path.join(self.directory, some_file)
        with Image.open(filepath) as img:
            metadata = {
                'filename': some_file,
                'format': img.format,
                'size': f"{img.width}x{img.height}",
                'mode': img.mode,
            }

        return metadata

    def save_to_csv(self) -> None:
        """Зберігає метадані всіх зображень у CSV-файл."""
        if not self.image_files:
            print(f"Каталог '{self.directory}' не містить зображень.")
            return

        with open(self.csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['filename', 'format', 'size', 'mode']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for metadata in self:
                writer.writerow(metadata)
        print(f"Метадані збережено у файл: {self.csv_file}")


# Використання
image_directory = "Screenshots"  # Вкажіть шлях до каталогу з вашими зображеннями
collector = MetadataImagesCollector(image_directory)
collector.save_to_csv()
