def solution(myString):
    answer = []
    string = myString.split('x')
    for i in string:
        answer.append(len(i))
    return answer