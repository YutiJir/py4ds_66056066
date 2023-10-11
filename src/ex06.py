"""
Execise 6
"""


def ordinal_suffix(param):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # TODO : complete this
    if param % 10 == 1:
        return '11st'
    elif param % 10 == 2:
        return 'nd'
    elif param % 10 == 3:
        return param +'rd'
    else:
        return param +'th'

