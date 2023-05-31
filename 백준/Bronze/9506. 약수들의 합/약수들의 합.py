while True:
    N = int(input())
    if N == -1:
        break
    answer = []
    
    for i in range(1, N):
        if N % i == 0:
            answer.append(i)
    
    if sum(answer) == N:
        print(N, " = ", " + ".join(str(i) for i in answer), sep="")
    else:
        print(f'{N}' + ' is NOT perfect.')