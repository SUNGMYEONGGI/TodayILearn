N = int(input())
data = []

for _ in range(N):
    number = int(input())
    data.append(number)
data.sort()

for i in data:
    print(i)