n = int(input())
data = list(map(int, input().split()))
data.sort()

print(max(data)-min(data))