n = int(input())

for _ in range(n):
    data = list(map(int, input().split(',')))
    print(sum(data))