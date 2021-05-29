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

    Paramters
    ---------
    val: number
        The number which is being double.

    Returns
    -------
    The number times two.
    """
    return val * 2


def subtract_one(val):
    """
    Subtract one from a number.

    Paramters
    ---------
    val: number
        The number which is being subtracted from.

    Returns
    -------
    The number subtract one.
    """
    return val - 1

def create_array(m, n):
    import numpy as np
    """
    Shirley
    Create an array of zeros

    Parameters
    --------
    m: the number of rows in the array
    n: the number of columns in the array

    Returns
    --------
    An mxn array of zeros
    """
    array=np.zeros(m,n)
    return array
