def solution(arr):
    arr_list1, arr_list2 = [], []
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr_list1.append(arr[i][j])
            arr_list2.append(arr[j][i])
            
    if arr_list1 == arr_list2:
        return 1
    else:
        return 0
            