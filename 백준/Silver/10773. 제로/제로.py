import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    money = int(input())
    if money > 0:
        stack.append(money)
    else:
        stack.pop()
print(sum(stack))