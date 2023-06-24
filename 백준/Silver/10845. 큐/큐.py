# push X: 정수 X를 큐에 넣는 연산이다.
# popleft: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다
import sys
from collections import deque

quque = deque()

N = int(sys.stdin.readline())
for _ in range(N):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        quque.append(data[1])
    elif data[0] == 'pop':
        if len(quque) > 0:
            print(quque[0])
            quque.popleft()
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(quque))
    elif data[0] == 'empty':
        if len(quque) > 0:
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if len(quque) > 0:
            print(quque[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if len(quque) > 0:
            print(quque[-1])
        else:
            print(-1)