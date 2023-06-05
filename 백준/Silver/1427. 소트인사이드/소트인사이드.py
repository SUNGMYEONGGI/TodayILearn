N = input()
data = []

for i in N:
    data.append(i)
data.sort(reverse=True)

print(''.join(data))