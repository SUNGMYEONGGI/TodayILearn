import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())

for i in range(1, n + 1):
    queue.append(i)

while True:
    if len(queue) == 1:
        break
    if len(queue) > 1:
        queue.popleft()
        if len(queue) == 1:
            break
        tmp = queue[0]
        queue.append(tmp)
        queue.popleft()

print(queue[0])
