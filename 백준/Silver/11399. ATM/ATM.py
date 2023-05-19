n = int(input())
AtmList = list(map(int, input().split()))
AtmList.sort()
# 과거(n) + 현재(n)
number = 0
result = 0

for i in range(n):
    number += AtmList[i]
    # print('number의 값: ', number)
    result += number

print(result)