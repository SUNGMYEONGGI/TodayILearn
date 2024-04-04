data = [list(str(input())) for _ in range(5)]

lenth = len(data[0])
for i in data:
    if lenth < len(i):
        lenth = len(i)

for j in data:
    if len(j) != lenth:
        for k in range(lenth-len(j)):
            j.append('')
answer = ''

for i in range(lenth):
    for j in range(5):
        answer += data[j][i]

print(answer)
