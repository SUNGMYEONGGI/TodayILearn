def solution(arr, flag):
    length = len(arr)
    answer = []
    for i in range(length):
        if flag[i] == True:
            answer.extend([arr[i]] * (arr[i] * 2))
        elif flag[i] == False:
            answer = answer[:-arr[i]]
    return answer