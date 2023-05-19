def solution(my_string, index_list):
    string = list(my_string)
    result = []
    for j in index_list:
        result.append(string[j])
    return ''.join(result)