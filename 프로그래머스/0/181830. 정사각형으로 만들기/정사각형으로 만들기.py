def solution(arr):
    k = max(len(arr), len(arr[0]))
    answer = []
    data = []
    cnt = 0
    while True:
        if cnt == len(arr):
            break
        for i in arr:
            for j in i:
                data.append(j)
            if len(data) != k:
                for lenth in range(k-len(i)):
                    data.append(0)
            answer.append(data)
            data = []
            cnt += 1
            if cnt == len(arr):
                break
                    
    if len(answer) != len(arr[0]):
        for _ in range(len(arr[0]) - len(arr)):
            data = [0] * len(arr[0])
            answer.append(data)
            
    return answer
