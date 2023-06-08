def solution(my_strings, parts):
    result = ''
    
    for i in range(len(my_strings)):
        for j in range(parts[i][0], parts[i][1] + 1):
            result += my_strings[i][j]
            
    return result