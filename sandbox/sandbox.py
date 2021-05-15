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
    The value from the Fibonnacci series at the given index.
    """
    if (index < 0):
        raise IndexError("Invalid Fibonacci Index")
        return -1
    if (index == 0):
        return 0
    else:
        im2 = 0  # Value of at index i-2
        im1 = 1  # Value of at index i-1
        for count in range(index-1):
            i = im2 + im1  # Sum the previous 2 numbers
            im2 = im1     # Move i-1 to i-2
            im1 = i       # Move i to i-1
        return im1  # Return the latest i (now in i-1)
