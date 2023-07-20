minkuk = list(map(int, input().split()))
mansae = list(map(int, input().split()))

S = sum(minkuk)
T = sum(mansae)

if S != T:
    print(max(S, T))
elif S == T:
    print(S)