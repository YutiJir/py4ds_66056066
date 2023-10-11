"""
Exercise 11
"""


def get_hr_min_sec(time):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """

    sec = time % 60
    min = time // 60 % 60
    hr = time // 60 // 60
    result = []
    if time == 0:
        return '0s'
    if hr > 0:
        result.append(str(hr) + 'h')
    if min > 0:
        result.append(str(min) + 'm')
    if sec > 0:
        result.append(str(sec) + 's')
    return ' '.join(result)

