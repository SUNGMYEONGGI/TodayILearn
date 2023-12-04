credit = [500, 100, 50, 10, 5, 1]

n = int(input())
remain_money = 1000-n
count = 0

for i in credit:
    if remain_money == 0:
        break
    if remain_money >= i:
        count += (remain_money//i)
        remain_money -= i*(remain_money//i)

print(count)