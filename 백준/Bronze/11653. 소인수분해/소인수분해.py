num = int(input())
N = 2

while num != True:
    if num % N == 0:
        print(N)
        num //= N
    else:
        N += 1