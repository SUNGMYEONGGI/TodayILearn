# 5분 ,1분, 10초

n = int(input())
n1, n2, n3 = 0, 0, 0

n1 = n//300
n = n%300
n2 = n//60
n = n%60
n3 = n//10
n = n%10

if n == 0:
    print(n1, n2, n3)
elif n != 0:
    print(-1)