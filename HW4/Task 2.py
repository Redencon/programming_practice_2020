def lcd(a: int, b: int):

    """
    Returns the least common divider of two positive integers as an integer
    If any of arguments is negative or not integer, returns None
    """

    if not isinstance(a, int) or not isinstance(b, int):
        return None
    if a < 0 or b < 0:
        return None
    rez = 1
    for i in range(1, a + 1):
        if b % i == 0 and a % i == 0:
            rez = i
    return rez
