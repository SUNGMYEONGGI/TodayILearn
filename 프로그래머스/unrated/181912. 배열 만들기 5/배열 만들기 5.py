def solution(intStrs, k, s, l):
    data = []
    for i in intStrs:
        if int(i[s:l+s]) > k:
            data.append(int(i[s:l+s]))
        
    return data