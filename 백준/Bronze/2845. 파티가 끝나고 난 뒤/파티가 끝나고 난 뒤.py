n1, n2 = map(int, input().split())
data = list(map(int, input().split()))

n = n1*n2
for i in data:
    print(i-n, end=' ')