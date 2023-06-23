def solution(a, b, c):
    if a != b and b != c and c != a:
        return a+b+c
    elif a == b:
        if b != c:
            return (a+b+c) * (a**2 + b**2 + c**2)
        elif b == c:
            return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif b == c:
        if c != a:
            return (a+b+c) * (a**2 + b**2 + c**2)
        elif a == c:
            return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif c == a:
        if a != b:
            return (a+b+c) * (a**2 + b**2 + c**2)
        elif b == a:
            return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)