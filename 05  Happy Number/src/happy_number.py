def is_happy(n : int) -> str:
    """Checks whether a given number is happy or not.

    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum
    of the squares of its digits in base-ten, and repeat the process
    until the number either equals 1 (where it will stay), or it loops
    endlessly in a cycle that does not include 1. Those numbers for
    which this process ends in 1 are happy numbers.

    :param n: The number to check.
    :type n: int
    :returns: True if the number is a happy number, False otherwise
    :rtype: bool

    :Example:

    >>> is_happy(19)
    True

    >>> is_happy(2)
    False
    """
    my_set = set()
    while n != 1 and n not in my_set:
        my_set.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1


if __name__ == "__main__":
    assert is_happy(4) is False
    assert not is_happy(7) is False
    assert is_happy(45) is False
    assert is_happy(44) is True
    print('All test cases pass')       



