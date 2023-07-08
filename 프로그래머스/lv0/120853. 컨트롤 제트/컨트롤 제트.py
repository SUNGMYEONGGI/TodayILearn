def solution(s):
    s = s.split(' ')
    result = 0
    
    for i in range(len(s)):
        if s[i] == "Z":
            result -= int(s[i-1])
        elif s[i] != "Z":
            result += int(s[i])
    
    return result