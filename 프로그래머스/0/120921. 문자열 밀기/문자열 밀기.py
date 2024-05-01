from collections import deque

def solution(A, B):
    Aqueue = deque(A)
    Bqueue = deque(B)
    # print(f'A와B의 덱 리스트 입니다. {Aqueue} {Bqueue}')
    for i in range(len(A)):
        if Aqueue == Bqueue:
            return i
        Aqueue.rotate(1)
    return -1
        