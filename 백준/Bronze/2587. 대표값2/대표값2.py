data = []

for _ in range(5):
    num = int(input())
    data.append(num)
data.sort()

print((sum(data) // 5))
print(data[2])