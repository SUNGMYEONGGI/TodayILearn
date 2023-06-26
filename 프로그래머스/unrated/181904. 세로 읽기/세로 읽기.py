def solution(my_string, m, c):
    data = []
    k = []
    cnt = 0
    for i in my_string:
        k.append(i)
        cnt += 1
        if cnt == m:
            data.append(k)
            cnt = 0
            k = []
    
    result = ''
    for j in range(len(data)):
        result += data[j][c-1]
    return result
        
        