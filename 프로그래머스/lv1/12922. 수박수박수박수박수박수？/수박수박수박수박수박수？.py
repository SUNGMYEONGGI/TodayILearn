def solution(n):
    answer = ''
    k = n // 2
    if n % 2 == 0:
        answer += ("수박"*k)
        return answer
    elif n % 2 != 0:
        answer += ("수박"*k)
        answer += "수"
        return answer