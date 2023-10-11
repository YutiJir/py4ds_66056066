"""
Execise 12
"""


def get_smallest(num):
    """
    Get the smallest number from a list of numbers.

    Args:
        num_list (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """
    if len(num) == 0:
        return None
    else:
        return int(min(num))

