def area_triangle(a: float, h: float) -> float:
    """
    Calculates the area of the triangle using it's height and base length
    """

    return 0.5 * a * h


def area_rectangle(a: float, b: float) -> float:
    """
    Calculates the area of the rectangle using the lengths of it's sides
    """

    return a * b


def area_circle(r: float) -> float:
    """
    Calculates the area of the circle using it's radius. The pi is 3.141592653589793
    """

    return 3.141592653589793 * r * r


def area_of_choice(x, y=1, *, shape: str = 'circle'):

    """
    Returns the area of some figure, determined by the user. Possible shapes are: triangle, rectangle, circle
    Abnormal values return None
    By default calculates the are of the circle of given radius
    """

    if not isinstance(shape, str) or not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
        return None
    elif x < 0 or y < 0:
        return None
    if shape == 'rectangle':
        return area_rectangle(x, y)
    elif shape == 'triangle':
        return area_triangle(x, y)
    elif shape == 'circle':
        return area_circle(x)
    else:
        return None


print(area_of_choice(18, 3, shape='triangle'))
print(area_of_choice(4, shape='circle'))
print(area_of_choice(5))
print(area_of_choice(3, 4, shape='rectangle'))
