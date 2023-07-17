n = int(input())
data = list(map(int, input().split()))
new_data = []
result = 0
result_data = []
for i in enumerate(data):
    new_data.append(i)

new_data = sorted(new_data, key=lambda x:x[1])

for j in range(len(new_data)):
    result += new_data[j][1]
    result_data.append(result)
    
print(sum(result_data))