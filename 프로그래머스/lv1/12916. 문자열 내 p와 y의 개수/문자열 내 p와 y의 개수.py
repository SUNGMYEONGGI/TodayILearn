def solution(string):
    string = string.lower()
    p_count = string.count('p')
    y_count = string.count('y')
    
    if p_count == y_count:
        return True
    else:
        return False