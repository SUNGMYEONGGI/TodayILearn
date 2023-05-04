N = int(input())

for _ in range(N):
    K = int(input())
    num = list(map(int, input().split()))
    answer = 0
    for i in num:
        answer += i
    print(answer)