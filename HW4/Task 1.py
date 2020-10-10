def power(a: float, n: int) -> float:

    """
    Function taking a in the power of n, if n is integer
    """

    if n == 0:
        return 1
    elif n < 0:
        n = -n
        a = 1 / a
    rez = 1
    for i in range(n):
        rez *= a
    return rez


print(power(2, -3))
