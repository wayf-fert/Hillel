class UnknownOperationError(Exception):
    """Custom exception for unknown operations."""
    pass


def my_calculate(num1: float, num2: float, operation: str) -> float:
    """
    Performs an arithmetic operation on two numbers.

    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): The operation to perform (+, -, *, /).

    Returns:
        float: The result of the operation.

    Raises:
        UnknownOperationError: If the operation isn't supported.
        ZeroDivisionError: If division by zero occurs.
        OverflowError: If the result overflows the permissible range.
    """
    if operation == '+':
        result: float = num1 + num2
    elif operation == '-':
        result: float = num1 - num2
    elif operation == '*':
        result: float = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Dividing by zero is prohibited.")
        result: float = num1 / num2
    else:
        raise UnknownOperationError(f"Unknown operation: {operation}")

    # Check for overflow
    if 1e308 < result < -1e308:
        raise OverflowError("The result of the operation overflows the permissible range.")

    return result


def main() -> None:
    """Main function to start the calculator."""
    while True:
        try:
            expression: str = input("Enter an expression, exp. \'2 + 2\' (or 'q' to exit): ")
            if expression.lower() == "q":
                print("Glory to Ukraine, kozache! Goodbye!\U0001F917")
                break

            parts: list[str] = expression.split()
            if len(parts) != 3:
                raise ValueError("Wrong format. Example of correct format: \'2 + 2\'.")

            num1: float = float(parts[0])
            operation: str = parts[1]
            num2: float = float(parts[2])

            result: float = my_calculate(num1, num2, operation)
            print(f"Result: {num1} {operation} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"ERROR: {e}\n")
        except ValueError as e:
            print(f"ERROR: {e}\n")
        except UnknownOperationError as e:
            print(f"ERROR: {e}\n")
        except OverflowError as e:
            print(f"ERROR: {e}\n")
        except Exception as e:
            print(f"ERROR: {e}\n")


if __name__ == "__main__":
    main()
