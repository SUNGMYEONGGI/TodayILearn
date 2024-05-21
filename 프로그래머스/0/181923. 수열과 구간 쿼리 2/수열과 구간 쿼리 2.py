def solution(arr, queries):
    data = []
    data2 = []
    for i in queries:
        for j in range(i[0], i[1]+1):
            if arr[j] > i[2]:
                data2.append(arr[j])
        if len(data2) > 0:
            data.append(min(data2))
            data2 = []
        else:
            data.append(-1)
        
    return data   