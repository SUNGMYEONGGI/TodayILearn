import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    data = list(map(str, sys.stdin.readline().split()))
    if data[0] == '1':
        stack.append(int(data[1]))
    elif data[0] == '2':
        if len(stack) > 0:
            tmp = stack[-1]
            stack.pop()
            print(tmp)
        else:
            print(-1)
    elif data[0] == '3':
        print(len(stack))
    elif data[0] == '4':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif data[0] == '5':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)