def solution(myString):
    answer = []
    for i in range(len(list(myString))):
        if myString[i] < 'l':
            answer.append('l')
        else:
            answer.append(myString[i])
    return ''.join(answer)
        