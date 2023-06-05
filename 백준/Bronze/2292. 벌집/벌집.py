N = int(input())

cnt = 1
k = 1
for _ in range(N):
    if N > 1:
        N -= (6*k)
        cnt += 1
        k += 1
    else:
        break

print(cnt)