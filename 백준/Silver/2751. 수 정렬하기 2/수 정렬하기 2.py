import sys

N = int(sys.stdin.readline())
data = []

for _ in range(N):
    number = int(sys.stdin.readline())
    data.append(number)
data.sort()

for i in data:
    print(i)