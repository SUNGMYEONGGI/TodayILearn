n = int(input())
data = []

for _ in range(n):
    k = list(map(str, input().split()))
    data.append(k)

agedata1 = sorted(data, key = lambda x : int(x[0]))

for i, j in agedata1:
    print(int(i), j)