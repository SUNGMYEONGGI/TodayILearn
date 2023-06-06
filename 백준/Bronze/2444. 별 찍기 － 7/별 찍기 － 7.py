N = int(input())

for i in range(1, N+1):
    print(" "*(N-i)+"*"*(i*2-1))
for j in reversed(range(1, N)):
    print(" "*(N-j)+"*"*(j*2-1))