def solution(n):
    result_odd = 0
    result_even = 0
    
    if n % 2 != 0:
        for i in range(1, n+1, 2):
            result_odd += i
        return result_odd
    elif n % 2 == 0:
        for i in range(0, n+1, 2):
            i *= i
            result_even += i
        return result_even