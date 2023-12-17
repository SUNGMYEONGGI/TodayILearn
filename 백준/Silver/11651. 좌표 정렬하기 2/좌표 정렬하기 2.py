n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dotlist1 = sorted(data, key = lambda x : x[0])
dotlist2 = sorted(dotlist1, key = lambda x : x[1])

for i, j in dotlist2:
    print(i, j)