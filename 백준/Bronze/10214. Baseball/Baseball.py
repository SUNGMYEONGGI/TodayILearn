N = int(input())
for _ in range(N):
    ys = 0
    ko = 0
    for i in range(9):
        ys_score, ko_score = map(int, input().split())
        ys += ys_score
        ko += ko_score

    if ys > ko:
        print('Yonsei')
    elif ys < ko:
        print('Korea')
    else:
        print('Draw')