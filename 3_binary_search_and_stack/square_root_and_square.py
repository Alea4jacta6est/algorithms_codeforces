def find_root(equation, left: float, right: float) -> int:
    x = (right + left) / 2
    while (right - left) > 0.0000001:
        x = (right + left) / 2
        if equation(x) > 0:
            right = x
        elif equation(x) < 0:
            left = x
        else:
            return x
    return round(x, 7)


c = float(input())
equation = lambda x: x**2 + x ** (1 / 2) - c
print(find_root(equation, 0, 100000))
