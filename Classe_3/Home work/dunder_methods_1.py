import math


class Fraction:
    """
    Клас для представлення дробу (чисельник/знаменник) та виконання арифметичних операцій з ним.

    Атрибути:
        numerator (int): Чисельник дробу.
        denominator (int): Знаменник дробу.

    Methods:
        __add__(self, other): Додає два дроби.
        __sub__(self, other): Віднімає один дріб від іншого.
        __mul__(self, other):  Перемножує два дроби.
        __truediv__(self, other): Ділить один дріб на інший.
        __repr__(self): Повертає рядкове представлення дробу у форматі «чисельник/знаменник»..
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Ініціалізація Fraction object.

        Args:
            numerator (int): Чисельник дробу.
            denominator (int): Знаменник дробу. Не повинен бути нулем.

        Raises:
            ValueError: Якщо знаменник дорівнює нулю.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other):
        """
        Додавання двох дробів.

        Args:
            other: дріб для додавання.

        Returns:
            Fraction: Результат додавання у вигляді спрощеного дробу.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Віднімання дробів.

        Args:
            other: дріб для віднімання.

        Returns:
            Fraction: Результат віднімання у вигляді спрощеного дробу.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Множення дробів.

        Args:
            other: дріб для множення.

        Returns:
            Fraction: Результат множення у вигляді спрощеного дробу.
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        Ділення дробів.

        Args:
            other: дріб для ділення.

        Returns:
            Fraction: Результат ділення у вигляді спрощеного дробу.

        Raises:
            ZeroDivisionError: якщо дріб дорівнює нулю (numerator=0).
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __repr__(self):
        """
        Returns:
            str: Дріб у форматі «чисельник/знаменник".
        """
        return f"{self.numerator}/{self.denominator}"


while True:
    fract1 = Fraction(int(input("Введи 1й чисельник: ")), int(input("Введи 1й знаменник: ")))
    fract2 = Fraction(int(input("Введи 2й чисельник: ")), int(input("Введи 2й знаменник: ")))

    print("\nРішення")

    # Додавання двох дробів
    print(f"{fract1} + {fract2} = {fract1 + fract2}")

    # Віднімання двох дробів
    print(f"{fract1} - {fract2} = {fract1 - fract2}")

    # Множення двох дробів
    print(f"{fract1} * {fract2} = {fract1 * fract2}")

    # Ділення двох дробів
    print(f"{fract1} / {fract2} = {fract1 / fract2}")
