import sys

N = int(sys.stdin.readline())
data = []

for _ in range(N):
    dot = list(map(int, sys.stdin.readline().split()))
    data.append(dot)
data.sort()

for i in data:
    print(i[0], i[1])