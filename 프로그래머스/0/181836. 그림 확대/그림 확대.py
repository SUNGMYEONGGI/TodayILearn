def solution(picture, k):
    data = []
    sent = ''
    for i in picture:
        i = list(i)
        for j in range(len(i)):
            sent += (i[j]*k)
            if j == len(i)-1:
                for _ in range(k):
                    data.append(sent)
                sent = ''

    return data