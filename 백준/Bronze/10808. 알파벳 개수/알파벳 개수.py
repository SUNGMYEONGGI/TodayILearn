s = input()
data = [0] * 26

for i in range(97, 123):
    for j in s:
        if chr(i) == j:
            data[i-97] += 1

data = ' '.join(map(str, data))
print(data)