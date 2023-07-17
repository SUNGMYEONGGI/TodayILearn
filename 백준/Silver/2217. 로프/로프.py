# 루프 수
k = int(input())
# 루프 저장 데이터
ropedata = []

for _ in range(k):
    rope_len = int(input())
    ropedata.append(rope_len)
    
ropedata.sort(reverse=True)

new_ropedata = []
for i in enumerate(ropedata):
    max_rope_len = (i[0]+1) * i[1]
    new_ropedata.append(max_rope_len)

print(max(new_ropedata))