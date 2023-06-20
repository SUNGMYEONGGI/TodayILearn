def solution(a, d, included):
    answer = 0
    for i in included:
        if i == True:
            answer += a
            a += d
        elif i == False:
            a += d
    return answer