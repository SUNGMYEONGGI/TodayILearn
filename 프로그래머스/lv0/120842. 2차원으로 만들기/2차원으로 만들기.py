def solution(num_list, n):
    answer = []
    result = []
    number = 1
    for i in num_list:
        if number != n:
            answer.append(i)
            number += 1
        elif number == n:
            answer.append(i)
            result.append(answer)
            answer = []
            number = 1
    return result