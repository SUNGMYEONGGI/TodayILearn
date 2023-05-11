def solution(my_string):
    answer = []
    banana = list(my_string)
    for i in range(len(banana)):
        answer.append(''.join(banana[i:]))
    answer.sort()
    return answer