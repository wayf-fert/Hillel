class Person:
    def __init__(self, name: str, age: int):
        """
        Ініціалізація об'єкта Person.
        :param name: Ім'я людини
        :param age: Вік людини
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я має бути непустим рядком.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Вік має бути невід'ємним цілим числом.")
        self.name = name.strip()
        self.age = age

    def __gt__(self, other) -> bool:
        """Порівняння двох об'єктів Person за віком (більше)."""
        return self.age > other.age

    def __lt__(self, other) -> bool:
        """Порівняння двох об'єктів Person за віком (менше)."""
        return self.age < other.age

    def __eq__(self, other) -> bool:
        """Перевірка рівності віку двох об'єктів Person."""
        return self.age == other.age

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


# List obj for class Person
people = [
    Person("Van Helsing", 45),
    Person("Anna Valerious", 25),
    Person("Vladislav Dracula", 400),
    Person("Carl", 30),
    Person("Frankenstein's Monster", 1),
]

# Сортування списку об'єктів за віком
sorted_people = sorted(people)

# Вивід результатів
print("List before sorted:")
for person in people:
    print('\t', person)

print("\nList after sorted by age:")
for person in sorted_people:
    print('\t', person)
