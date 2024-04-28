import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()

for i in reversed(range(1, n+1)):
    queue.appendleft(i)
    if len(queue) > 1:
        cnt = 0
        while True:
            if cnt == i:
                break
            queue.appendleft(queue[-1])
            # print(queue)
            queue.pop()
            # print(queue)            
            cnt += 1
    elif len(queue) == 1:
        continue
print(*queue)