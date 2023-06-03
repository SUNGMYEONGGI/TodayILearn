N, M = map(int, input().split())
Data_A, Data_B = [], []

for _ in range(N):
    A = list(map(int, input().split()))
    Data_A.append(A)
    
for _ in range(N):
    B = list(map(int, input().split()))
    Data_B.append(B)

for i in range(N):
    for j in range(M):
        print(Data_A[i][j] + Data_B[i][j], end=' ')
    print('')