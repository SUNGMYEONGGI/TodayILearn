N = int(input())
cnt = 1

if N == 0:
    print(cnt)
else:
    for i in range(1, N+1):
        cnt *= i
    print(cnt)