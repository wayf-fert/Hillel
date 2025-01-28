from typing import Iterator


def log_file_error_generator(file_path: str) -> Iterator[str]:
    """
    Генератор для зчитування лог-файлу рядок за рядком
    та повернення лише рядків з помилками (код статусу 4XX або 5XX).

    Args:
        file_path (str): Шлях до лог-файлу.

    Yields:
        str: Рядок з лог-файлу, що містить помилку.
    """
    with open(file_path, 'r') as log_file:
        for line in log_file:
            parts = line.split()
            if len(parts) > 3 and parts[5].isdigit():
                status_code = int(parts[5])
                if 400 <= status_code < 600:
                    yield line


def save_errors_to_file(input_filepath: str, output_filepath: str) -> None:
    """
    Зберігає рядки з помилками з лог-файлу в окремий файл.

    Args:
        input_filepath (str): Шлях до вхідного лог-файлу.
        output_filepath (str): Шлях до файлу, куди зберігатимуться помилки.
    """
    with open(output_filepath, 'w') as output_file:
        for error_line in log_file_error_generator(input_filepath):
            output_file.write(error_line)
    print(f"Помилки збережено у файл: {output_filepath}")


# input_file = input("Введіть шлях до каталогу: ")
input_file = "/Users/pavel/EDU/Hillel/Class4/task_4/task_4_file_path.log"
output_file = "task_7_errors_for_analitics.log"

save_errors_to_file(input_file, output_file)
