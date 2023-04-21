N = int(input())
count_ag = 0
count_op = 0

for _ in range(N):
    num1 = int(input())
    if num1 == 1:
        count_ag += 1
    elif num1 == 0:
        count_op += 1

if count_ag > count_op:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')