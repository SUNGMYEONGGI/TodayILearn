import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    data = sys.stdin.readline().split()
    if data[0] == '1':
        queue.appendleft(int(data[1]))
    elif data[0] == '2':
        queue.append(int(data[1]))
    elif data[0] == '3':
        if len(queue) > 0:
            tmp = queue[0]
            queue.popleft()
            print(tmp)
        else:
            print(-1)
    elif data[0] == '4':
        if len(queue) > 0:
            tmp = queue[-1]
            queue.pop()
            print(tmp)
        else:
            print(-1)
    elif data[0] == '5':
        print(len(queue))
    elif data[0] == '6':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif data[0] == '7':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif data[0] == '8':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)