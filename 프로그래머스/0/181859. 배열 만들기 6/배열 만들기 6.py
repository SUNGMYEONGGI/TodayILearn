def solution(arr):
    stk = []
    cnt = 0
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
            cnt += 1
        elif len(stk) > 0:
            if arr[i] == stk[-1]:
                stk.pop()
                cnt += 1
            elif arr[i] != stk[-1]:
                stk.append(arr[i])
                cnt += 1
    if len(stk) > 0:
        return stk
    else:
        return [-1]