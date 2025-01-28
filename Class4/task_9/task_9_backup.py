import os


class BackupManager:
    """
    Контекстний менеджер для створення резервної копії файлу перед його обробкою.

    Attributes:
        filepath (str): Шлях до оригінального файлу.
        backup_filepath (str): Шлях до резервної копії файлу.
    """

    def __init__(self, filepath: str) -> None:
        """
        Ініціалізує менеджер резервних копій для файлу.

        Args:
            filepath (str): Шлях до оригінального файлу.
        """
        self.filepath = filepath
        self.backup_filepath = f"{filepath}.bak"  # Визначення шляху до резервної копії

    def __enter__(self) -> str:
        """
        Створює резервну копію файлу перед входом у контекст.

        Returns:
            str: Шлях до оригінального файлу для подальшої обробки.
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Файл {self.filepath} не знайдено.")

        # Створюємо резервну копію файлу
        with open(self.filepath, 'rb') as src_file:
            with open(self.backup_filepath, 'wb') as backup_file:
                backup_file.write(src_file.read())

        return self.filepath

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Відновлює резервну копію у разі помилки або видаляє її після успішної обробки.

        Args:
            exc_type: Тип виключення, якщо виникло.
            exc_val: Значення виключення, якщо виникло.
            exc_tb: Трасування виключення, якщо виникло.
        """
        if exc_type:
            with open(self.backup_filepath, 'rb') as backup_file:
                with open(self.filepath, 'wb') as src_file:
                    src_file.write(backup_file.read())
            os.remove(self.backup_filepath)
            raise exc_val
        else:

            os.remove(self.backup_filepath)


file_path = "task_9_important_file.txt"

with open(file_path, 'w') as file:
    file.write("Important data\n")

with BackupManager(file_path) as file:
    with open(file, 'w') as f:
        f.write("New data.\n")

    raise Exception("Simulate ERROR")

with open(file_path, 'r') as file:
    print(file.read())
