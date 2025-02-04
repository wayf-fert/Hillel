from my_package.math_utils import factorial, gcd
from my_package.string_utils import uppercase_string, remover_spaces


def main():
    """DEMO work functions from file math_utils.py"""
    number_factorial = int(input("Enter number factorial n: "))
    print(f"Factorial {number_factorial}: {factorial(number_factorial)}\n")

    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    print(f"GSD for {first_num} and {second_num}: {gcd(first_num, second_num)}\n")

    """DEMO work functions from file string_utils.py"""
    some_text = input("Enter your text: ")
    print(f"Your text in upper case: \'{uppercase_string(some_text)}\'")
    print(f"Your text without spaces at the beginning and end of the line: \'{remover_spaces(some_text)}\'")


if __name__ == "__main__":
    main()
