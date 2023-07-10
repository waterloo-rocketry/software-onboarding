def add_one(val):
    """
    Add one to a number.

    Parameters
    ----------
    val: number
        The number to which one should be added.

    Returns
    -------
    The number plus one.
    """
    return val + 1


def add_two(val):
    """
    Add 2 to a number.

    Parameters
    ----------
    val: number
        The number to which two should be added.

    Returns
    -------
    The number plus two.
    """
    return val + 2


def fibonacci_by_index(index: int):
    """
    Get the value at the index of the Fibonacci series.

    Austin W. Milne @awbmilne  <austin.milne@uwaterloo.ca>

    Parameters
    ----------
    index: number
        The index of the Fibonacci series to return.

    Returns
    -------
    The value from the Fibonacci series at the given index.
    """
    if (index < 0):
        raise IndexError("Invalid Fibonacci Index")
    else:
        i = 0    # Value at index i
        ip1 = 1  # Value at index i+1
        for count in range(index):
            ip2 = i + ip1  # i+2 is the sum of i and i+1
            i = ip1        # Move i+1 to i
            ip1 = ip2      # Move i+2 to i+1
        return i  # Return i


def multiply_by_two(val):
    """
    Multiply a number by two.

    Parameters
    ----------
    val: number
        The number which is being double.

    Returns
    -------
    The number times two.
    """
    return val * 2


def factorial(integer):
    """
    Return the factorial of a position integer.

    Parameters
    ----------
    integer: an integer

    Returns
    -------
    the value of the factorial
    """
    if integer == 0:
        return 1
    else:
        return integer * factorial(integer-1)


def subtract_one(val):
    """
    Subtract one from a number.

    Parameters
    ----------
    val: number
        The number which is being subtracted from.

    Returns
    -------
    The number subtract one.
    """
    return val - 1


def area_of_rect(length, width):
    """
    Calculates the area of a rectangle.

    Parameters
    ----------
    length: number
        The length of the rectangle.
    width: number
        The width of the rectangle.

    Returns
    -------
    The area of the rectangle.
    """
    return length * width


def single_number(integers):
    """
    Given a non-empty array of integers, every element
    appears twice except for one. This function finds
    that single one.

    Parameters
    ----------
    integers: array
        Non-empty array of integers

    Returns
    -------
    Single integer
    """

    single = 0

    for num in integers:
        single ^= num

    return single


def ceil_sqrt(x: int) -> int:
    """
    Given a non-negative integer, attempts to find the
    the square root of the integer, rounded up.
    Equivalent to ceiling(square_root(x))

    Parameters
    ----------
    x: non-negative integer
        Non-negative integer you want to sqrt

    Returns
    -------
    ceil(sqrt(x)): non-negative integer
    """

    i = 0

    while (i**2 < x):
        i += 1

    return i


def double_string(x: str) -> str:
    """
    Given a string, returns the string appended
    to itself. Equivalent to string + string.

    Parameters
    ----------
    x: string
        String that you want to double

    Returns
    -------
    The original string appended to itself
    """
    return x + x
