"""
Execise 4
"""


def area(length, weight):
    """
    Calculates the area of a rectangle given its length and width.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    # TODO : complete this
    return length * weight


def perimeter(length, weight):
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    # TODO : complete this
    return length+weight + length+weight


def volume(length, weight, height):
    """
    Calculates the volume of an object given its length, width, and height.

    Args:
        length (float): The length of the object.
        width (float): The width of the object.
        height (float): The height of the object.

    Returns:
        float: The volume of the object.
    """
    # TODO : complete this
    return length * weight * height


def surface_area(length, weight, height):
    """
    Calculate the surface area of a rectangular prism.

    Parameters:
        length (float): The length of the rectangular prism.
        width (float): The width of the rectangular prism.
        height (float): The height of the rectangular prism.

    Returns:
        float: The total surface area of the rectangular prism.
    """
    # TODO : complete this
    return 2 * (length * weight) + 2 * (weight * height) + 2 * (length * height)
