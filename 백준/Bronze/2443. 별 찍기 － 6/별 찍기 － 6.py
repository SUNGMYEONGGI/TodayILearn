n = int(input())
cnt = 0

for i in reversed(range(1, n+1)):
    print(' ' * cnt + '*' * i + '*'*(i-1))
    cnt += 1