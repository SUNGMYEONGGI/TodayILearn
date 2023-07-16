def solution(arr, k):
    data = []
    for i in arr:
        if i not in data:
            data.append(i)
    
    if len(data) > k:
        return data[:k]
    else:
        data = data[:len(data)]
        k_data = [-1] * (k - len(data))
        return data+k_data