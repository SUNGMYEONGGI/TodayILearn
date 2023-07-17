N = int(input())
meet_data = []

for _ in range(N):
    mt1, mt2 = map(int, input().split())
    k = (mt1, mt2)
    meet_data.append(k)

# x[0]을 우선 정렬    
meet_ascend_data = sorted(meet_data, key=lambda x:x[0])
# 정렬된 data를 다시 x[1]을 기준으로 정렬
meet_ascend_data = sorted(meet_ascend_data, key=lambda x:x[1])

starttime = 0
endtime = 0
meetable_data = []

for i in range(len(meet_ascend_data)):
    if endtime <= meet_ascend_data[i][0]:
        starttime = meet_ascend_data[i][0]
        endtime = meet_ascend_data[i][1]
        meetable_data.append(meet_ascend_data[i])

print(len(meetable_data))