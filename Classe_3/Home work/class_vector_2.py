import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float):
        """
        Ініціалізація вектора з двома координатами.
        :param coordinate_x: Перша координата вектора
        :param coordinate_y: Друга координата вектора
        """
        if not isinstance(coordinate_x, (int, float)) or not isinstance(coordinate_y, (int, float)):
            raise ValueError("Координати мають бути числовими значеннями (int або float).")
        self.coordinate_x = float(coordinate_x)
        self.coordinate_y = float(coordinate_y)

    def __add__(self, other):
        """Додавання двох векторів."""
        return Vector(self.coordinate_x + other.coordinate_x, self.coordinate_y + other.coordinate_y)

    def __sub__(self, other):
        """Віднімання двох векторів."""
        return Vector(self.coordinate_x - other.coordinate_x, self.coordinate_y - other.coordinate_y)

    def __mul__(self, scalar):
        """Множення вектора на число."""
        if not isinstance(scalar, (int, float)):
            raise ValueError("Множник має бути числом (int або float).")
        return Vector(self.coordinate_x * scalar, self.coordinate_y * scalar)

    def __eq__(self, other):
        """Перевірка на рівність двох векторів."""
        return (math.isclose(self.coordinate_x, other.coordinate_x)
                and math.isclose(self.coordinate_y, other.coordinate_y))

    def __lt__(self, other):
        """
        Порівняння двох векторів за довжиною.
        :return: True, якщо довжина поточного вектора менша
        """
        return self.length() < other.length()

    def length(self):
        """
        Обчислення довжини вектора.
        :return: Довжина вектора
        """
        return math.sqrt(self.coordinate_x ** 2 + self.coordinate_y ** 2)

    def __repr__(self) -> str:
        """
        Повертає текстове представлення вектора у форматі Vector(x, y).
        """
        return f"Vector({self.coordinate_x:.2f}, {self.coordinate_y:.2f})"


v1 = Vector(float(input("Введи координату вектора 'x_1': ")), float(input("Введи координату вектора 'y_1': ")))
v2 = Vector(float(input("Введи координату вектора 'x_2': ")), float(input("Введи координату вектора 'y_2': ")))

print("=" * 36)
print(f"Додавання: {v1 + v2}")
print(f"Віднімання: {v1 - v2}")
print(f"Множення на число 3: V_1 = {v1 * 3}, V_2 = {v2 * 3}")
print(f"Порівняння за довжиною (v1 < v2): {v1 < v2}")
print(f"Перевірка на рівність (v1 == v2): {v1 == v2}")
print(f"Довжина v1: {v1.length():.2f}")
print(f"Довжина v2: {v2.length():.2f}")
print("=" * 36)
