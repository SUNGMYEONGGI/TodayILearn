s = input().split('-')
data = []

for i in s:
    n = 0
    i = i.split('+')
    # print(i)
    for j in i:
        n += int(j)
    data.append(n)

k = data[0]
print(k-sum(data[1:]))