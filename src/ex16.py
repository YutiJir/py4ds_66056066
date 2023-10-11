"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    if len(num_list) == 0:
        return None

    max_count = 0
    mlist = []
    index = 0

    while index < len(num_list):
        num = num_list[index]
        count = num_list.count(num)
        if count > max_count:
            max_count = count
            mlist = [num]
        elif count == max_count:
            mlist.append(num)
        index += 1

    return mlist[0]
