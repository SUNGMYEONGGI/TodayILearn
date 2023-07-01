def solution(before, after):
    cnt = 0
    
    for i in before:
        for j in after:
            if i == j:
                cnt += 1
                after = after.replace(i, '', 1)
                break
    if len(before) == cnt:
        return 1
    else:
        return 0