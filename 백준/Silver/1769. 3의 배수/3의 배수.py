num = input()
# answer = 0
cnt = 0
while len(num) > 1:
    cnt += 1
    answer = 0
    for i in num:
        answer += int(i)
    num = str(answer)

    # print(f'{cnt}번 반복')
    # print(f'{cnt}번째 num의 값: {num}')

# print(cnt)
num = int(num)
if num % 3 == 0:
    print(cnt, 'YES', sep='\n')
else:
    print(cnt, 'NO', sep='\n')