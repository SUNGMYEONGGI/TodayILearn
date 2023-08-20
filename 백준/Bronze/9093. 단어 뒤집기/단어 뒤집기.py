n = int(input())
answer = ''
for _ in range(n):
    s = input()
    s = s.split(' ')
    # print(s)
    for i in s:
        answer += i[::-1]
        answer += ' '
    print(answer)
    answer = ''