import math


class Vector:
    def __init__(self, *coordinates):
        """
        Ініціалізація вектора з n координатами.
        :param coordinates: Координати вектора (числа типу int або float).
        """
        if not all(isinstance(coord, (int, float)) for coord in coordinates):
            raise ValueError("Всі координати мають бути числовими значеннями (int або float).")
        self.coordinates = tuple(float(coord) for coord in coordinates)

    def __add__(self, other):
        """Додавання двох векторів."""
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Вектори повинні мати однакову кількість вимірів для додавання.")
        return Vector(*(a + b for a, b in zip(self.coordinates, other.coordinates)))

    def __sub__(self, other):
        """Віднімання двох векторів."""
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Вектори повинні мати однакову кількість вимірів для віднімання.")
        return Vector(*(a - b for a, b in zip(self.coordinates, other.coordinates)))

    def __mul__(self, other):
        """Множення вектора на число або обчислення скалярного добутку двох векторів."""
        if isinstance(other, (int, float)):
            return Vector(*(coord * other for coord in self.coordinates))
        elif isinstance(other, Vector):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError("Вектори повинні мати однакову кількість вимірів для скалярного добутку.")
            return sum(a * b for a, b in zip(self.coordinates, other.coordinates))
        else:
            raise ValueError("Множення підтримується тільки для чисел або іншого вектора.")

    def __lt__(self, other):
        """Порівняння двох векторів за їх довжиною."""
        return self.length() < other.length()

    def length(self):
        """Обчислення довжини вектора."""
        return math.sqrt(sum(coord ** 2 for coord in self.coordinates))

    def __repr__(self) -> str:
        """Повертає текстове представлення вектора."""
        coords_str = ", ".join(f"{coord:.2f}" for coord in self.coordinates)
        return f"Vector({coords_str})"


v1 = Vector(1.3, 2, 3)
v2 = Vector(4, -5, 6)

print(f"Додавання: {v1 + v2}")
print(f"Віднімання: {v1 - v2}")
print(f"Скалярний добуток: {v1 * v2}")
print(f"Порівняння за довжиною (v1 < v2): {v1 < v2}")
