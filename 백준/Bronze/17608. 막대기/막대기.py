import sys

num = int(sys.stdin.readline())
data = []
for _ in range(num):
    stick = int(sys.stdin.readline())
    data.append(stick)

data = data[::-1]

stick_num = data[0]
cnt = 1
for i in range(1, len(data)):
    if stick_num < data[i]:
        cnt += 1
        stick_num = data[i]

print(cnt)