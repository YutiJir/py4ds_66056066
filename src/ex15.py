"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    n = len(num_list)
    num_list.sort()

    if n == 0:
        return None
    elif n % 2 == 0:
        med = n // 2
        return (num_list[med] + num_list[med - 1]) / 2
    else:
        med = n // 2
        return num_list[med]
