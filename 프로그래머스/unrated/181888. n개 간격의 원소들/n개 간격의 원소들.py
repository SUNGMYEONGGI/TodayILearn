def solution(num_list, n):
    answer = []
    result = 0
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer