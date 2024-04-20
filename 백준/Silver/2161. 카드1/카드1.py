import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
data = []
for i in range(1, n+1):
    queue.append(i)

while True:
    if len(queue) == 1:
        data.append(queue[0])
        break
    if len(queue) > 1:
        data.append(queue[0])
        queue.popleft()
        if len(queue) == 1:
            data.append(queue[0])
            break
        tmp = queue[0]
        queue.popleft()
        queue.append(tmp)
        
print(*data)