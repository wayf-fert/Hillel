def calculate_average_from_txt(my_file: str) -> float:
    """
    Reads numbers from a file and calculates their arithmetic mean.

    Args:
        my_file (str): Name of the file with numbers.

    Returns:
        float: Arithmetic mean of the numbers.

    Raises:
        FileNotFoundError: If the file is not found.
        ValueError: If the file is empty or contains invalid data.
    """
    try:
        with open(my_file, 'r') as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("ERROR: this file is empty.")

        numbers = []
        for line_number, line in enumerate(lines, 1):
            stripped_line = line.strip()
            if not stripped_line:  # Skip empty lines
                continue
            try:
                number = float(stripped_line)
                numbers.append(number)
            except ValueError:
                raise ValueError(f"Invalid data on line {line_number}: {stripped_line}")

        if not numbers:
            raise ValueError("This file does't contain any numbers.")

        if len(numbers) == 1:
            raise ValueError("The file contains only one number, unable to calculate average.")

        average = sum(numbers) / len(numbers)
        return average

    except FileNotFoundError as e:
        raise FileNotFoundError(f"File '{my_file}' not found.") from e
    except ValueError as e:
        raise e
    except Exception as e:
        raise Exception(f"Unknown error: {str(e)}") from e


if __name__ == "__main__":
    text_file = input("Enter the name of the file with numbers: ").strip()
    try:
        avg = calculate_average_from_txt(text_file)
        print(f"Arithmetic mean: {avg:.3f}")
    except Exception as e:
        print(f"Error: {e}")
