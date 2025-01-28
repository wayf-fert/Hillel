def keyword_filter(file_path: str, keyword: str):
    """Генератор, який повертає рядки, що містять певне ключове слово."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                yield line


def filter_and_write(input_file: str, output_file: str, keyword: str) -> None:
    """Фільтрує файл за ключовим словом та записує відповідні рядки у новий файл."""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in keyword_filter(input_file, keyword):
            outfile.write(line)
    print(f"Фільтровані рядки збережено у файл: {output_file}")


input_file_log = "task_4_file_path.log"
output_file_log = "task_4_path_source_file.log"
keyword = "ERROR"

filter_and_write(input_file_log, output_file_log, keyword)

with open(output_file_log, 'r', encoding='utf-8') as f:
    print("Відфільтровані рядки:")
    print(f.read())
