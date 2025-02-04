import csv
import os


def create_csv_if_not_exists(filename: str) -> None:
    """Creates a CSV file if it doesn't exist and adds the initial data."""
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Ім'я", "Вік", "Оцінка"])
            writer.writerows([
                ["Петро", "21", "90"],
                ["Марина", "22", "85"],
                ["Андрій", "20", "88"]
            ])


def read_students_from_csv(filename: str) -> list:
    """Read info abot students from CSV-file."""
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовки
            students = [row for row in reader]
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return students


def get_average_grade(students: list) -> float:
    """Average grade of students."""
    if not students:
        return 0.0
    average_grade = sum(float(student[2]) for student in students) / len(students)
    return average_grade


def add_student(filename: str, student_info: list[str]) -> None:
    """Add new students to CSV-file."""
    with open(filename, mode='a', newline='\n', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(student_info)


if __name__ == '__main__':
    list_students_info: str = 'students_info.csv'
    create_csv_if_not_exists(list_students_info)

    students = read_students_from_csv(list_students_info)

    if students:
        average_grade = get_average_grade(students)
        print(f'Average grade of students: {average_grade:.2f}')
    else:
        print('Students not found.')

    new_student_name = input("Enter new student name: ")
    while True:
        new_student_age = input("Enter new student age: ")
        if new_student_age.isdigit():
            break
        print("ERROR! Age must be number.")

    while True:
        new_student_grade = input("Enter grade the new students: ")
        try:
            float(new_student_grade)
            break
        except ValueError:
            print("ERROR! Grade must be number.")

    new_student_info = [new_student_name, new_student_age, new_student_grade]
    add_student(list_students_info, new_student_info)
    print(f"Student {new_student_name} added successful to CSV-file {list_students_info}.")
