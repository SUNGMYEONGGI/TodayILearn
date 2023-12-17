n = int(input())
data = []

for _ in range(n):
    data.append(input())

dp = []
for i, j in enumerate(range(len(data))):
    dp.append((len(data[j]), data[i]))

lendp1 = sorted(dp, key = lambda x : x[1])
lendp2 = sorted(lendp1, key = lambda x : x[0])

for k in range(0, len(lendp2)):
    if k > 0:
        if lendp2[k][1] != lendp2[k-1][1]:
            print(lendp2[k][1])
    else:
        print(lendp2[k][1])