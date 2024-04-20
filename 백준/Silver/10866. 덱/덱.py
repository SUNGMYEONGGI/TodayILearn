import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    data = sys.stdin.readline().split()
    if data[0] == 'push_front':
        queue.appendleft(int(data[1]))
    elif data[0] == 'push_back':
        queue.append(int(data[1]))
    elif data[0] == 'pop_front':
        if len(queue) > 0:
            tmp = queue[0]
            queue.popleft()
            print(tmp)
        else:
            print(-1)
    elif data[0] == 'pop_back':
        if len(queue) > 0:
            tmp = queue[-1]
            queue.pop()
            print(tmp)
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(queue))
    elif data[0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)