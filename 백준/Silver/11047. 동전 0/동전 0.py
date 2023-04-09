N, K = map(int, input().split())
result = 0
coin_list = []

for _ in range(N):
    won = int(input())
    coin_list.append(won)

for i in sorted(coin_list, reverse=True):
    if K == 0:
        break
    result += K//i
    K %= i

print(result)