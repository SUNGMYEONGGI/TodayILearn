def solution(arr, divisor):
    answer = []
    cnt = 0
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        elif i % divisor != 0:
            cnt += 1
            if cnt == len(arr):
                return [-1]
            else:
                continue
    answer.sort()
    return answer