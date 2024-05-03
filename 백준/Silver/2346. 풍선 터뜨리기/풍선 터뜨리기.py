import sys
from collections import deque

n = int(sys.stdin.readline())
balloon = enumerate(map(int, sys.stdin.readline().split()))
queue = deque(balloon)

data = []
while True:
    if len(queue) == 0:
        break
    cnt, num = queue.popleft()
    data.append(cnt+1)

    if num > 0:
        queue.rotate(-(num-1))
    elif num < 0:
        queue.rotate(-num)

print(*data)