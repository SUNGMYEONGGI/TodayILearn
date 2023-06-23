def solution(arr, intervals):
    result = []
    for i in range(len(intervals)):
        for j in range(intervals[i][0], intervals[i][1]+1):
            result.append(arr[j])
    return result
