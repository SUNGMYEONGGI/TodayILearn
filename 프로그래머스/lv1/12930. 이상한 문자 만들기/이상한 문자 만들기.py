def solution(s):
    data = ''
    s = s.split(' ')
    for i in s:
        data += ' '
        for j in range(len(i)):
            if j % 2 == 0:
                data += i[j].upper()
            else:
                data += i[j].lower()
    return data[1:]