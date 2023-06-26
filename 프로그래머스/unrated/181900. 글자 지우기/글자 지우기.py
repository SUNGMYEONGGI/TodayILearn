def solution(my_string, indices):
    data = []
    result = ''
    for i in range(0, len(my_string)):
        if i not in indices:
            data.append(i)
            
    for i in data:
        result += my_string[i]
    return result