A = int(input())
B = int(input())
C = int(input())

cnt = 0

for i in range(0, 10):
    cnt = str(A * B * C).count(str(i))
    print(cnt)
    cnt = 0