n, m = map(int, input().split())
data = []
answer = 0

for _ in range(n):
    money = int(input())
    data.append(money)


for i in reversed(data):
    if m//i > 0:
        answer += m//i
    m %= i

print(answer)