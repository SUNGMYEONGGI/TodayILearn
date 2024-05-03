def solution(s):
    if s[0] == ")" or s[-1] == "(":
        return False
    cnt = 0
    for i in reversed(s):
        if i == ")":
            cnt += 1
        elif i == "(":
            if cnt == 0:
                return False
                break
            cnt -= 1
    
    if cnt == 0:
        return True
    else:
        return False
        