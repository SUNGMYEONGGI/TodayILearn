import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

money = 1

for i in data:
    if money < i:
        break
    money += i

print(money)