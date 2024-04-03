n, m = map(int, input().split())
data = []

for i in range(1, m+1):
    data.append([i] * i)
data2 = []

for j in data:
    for k in j:
        data2.append(k)
print(sum(data2[n-1:m]))