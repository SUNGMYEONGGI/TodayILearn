def solution(str1, str2):
    answer = ''
    sent = str1 + str2
    for i in range(len(sent)-len(str1)):
        answer += sent[i]
        answer += sent[i+len(str1)]
    return answer