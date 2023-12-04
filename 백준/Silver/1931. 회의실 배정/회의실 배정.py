n = int(input())
data = []

for _ in range(n):
    time = map(int, input().split())
    data.append(tuple(time))

Sort_StartTime = sorted(data, key=lambda x: x[0])
Sort_EndTime = sorted(Sort_StartTime, key=lambda x: x[1])

endtime = 0
cnt = 0
for i in Sort_EndTime:
    if i[0] >= endtime:
        endtime = i[1]
        cnt += 1

print(cnt)