def factorial(n: int) -> int:
    """
    Factorial function
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def gcd(a: int, b: int) -> int:
    """
    The greatest common divisor (GCD) using the Euclidean algorithm common divisor

    Args:
        a: first number
        b: second number

    Returns:
        gsd: values a & b
    """
    while b != 0:
        a, b = b, (a % b)
    return abs(a)
