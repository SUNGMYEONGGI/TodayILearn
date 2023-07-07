def solution(dots):
    H = max(dots)[0] - min(dots)[0]
    V = max(dots)[1] - min(dots)[1]
    return H*V