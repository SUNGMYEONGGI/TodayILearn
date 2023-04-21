K, N, M = map(int, input().split())
SnackPrice = K * N

if (SnackPrice-M) > 0:
    print(SnackPrice-M) 
else:
    print('0')