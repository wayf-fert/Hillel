class BinaryNumber:
    """
    Клас для представлення двійкового числа.

    Args:
        value (int): Двійкове число, представлене як ціле число (0 або 1).

    Methods:
        __and__(self, other): Повертає результат операції AND для двох двійкових чисел.
        __or__(self, other): Повертає результат операції OR для двох двійкових чисел.
        __xor__(self, other): Повертає результат операції XOR для двох двійкових чисел.
        __invert__(self): Повертає результат операції NOT для двійкового числа.
        __repr__(self): Повертає рядкове представлення двійкового числа.
    """

    def __init__(self, value: int):
        """Ініціалізація BinaryNumber object."""

        if value not in (0, 1):
            raise ValueError("Binary number must be 0 or 1.")
        self.value = value

    def __and__(self, other):
        """
        Операція AND.

        Return:
            BinaryNumber: Результат операції AND.
        """
        return BinaryNumber(self.value & other.value)

    def __or__(self, other):
        """
        Операція OR.

        Return:
            BinaryNumber: Результат операції OR.
        """
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other):
        """
        Операція XOR.

        Returns:
            BinaryNumbe: Результат операції XOR.
        """
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self):
        """
        Операція NOT.

        Returns:
            BinaryNumber: Результат операції NOT.
        """
        return BinaryNumber(1 - self.value)

    def __repr__(self):
        return f"{self.value}"


# Тестування класу BinaryNumber
msg = int(input("Введіть перше двійкове число (0 або 1): "))
msg2 = int(input("Введіть друге двійкове число (0 або 1): "))

bin1 = BinaryNumber(msg)
bin2 = BinaryNumber(msg2)

print("\nРезультати операцій:")

# AND
print(f"{bin1} AND {bin2} = {bin1 & bin2}")

# OR
print(f"{bin1} OR {bin2} = {bin1 | bin2}")

# XOR
print(f"{bin1} XOR {bin2} = {bin1 ^ bin2}")

# NOT
print(f"NOT {bin1} = {~bin1}")
print(f"NOT {bin2} = {~bin2}")
