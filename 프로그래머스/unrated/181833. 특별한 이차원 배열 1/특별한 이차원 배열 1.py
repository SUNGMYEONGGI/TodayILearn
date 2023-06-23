def solution(n):
    result = []
    for i in range(n):
        newdata = [0] * n
        newdata[i] = 1
        result.append(newdata)
    return result