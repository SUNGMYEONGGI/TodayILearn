n = int(input())
cnt = 1

print('*'*n)
for i in reversed(range(1, n)):
    print(' '*cnt, end='')
    cnt += 1
    print('*'*i)