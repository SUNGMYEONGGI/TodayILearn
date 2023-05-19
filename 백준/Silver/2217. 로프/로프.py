k = int(input())
answer1 = []
for _ in range(k):
    n = int(input())
    answer1.append(n)
answer1.sort(reverse=True)

answer2 = []
number = 1
for i in answer1:
    i *= number
    number += 1
    answer2.append(i)

print(max(answer2))