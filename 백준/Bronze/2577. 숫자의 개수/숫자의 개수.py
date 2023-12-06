count = 1
num_list = [0 for _ in range(10)]
for _ in range(3):
    num = int(input())
    count *= num

for i in str(count):
    num_list[int(i)] += 1

for i in num_list:
    print(i)