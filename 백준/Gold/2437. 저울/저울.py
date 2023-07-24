import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

weight = 1

for i in data:
    if weight < i:
        break
    weight += i

print(weight)