import math

num = int(input())
k = format(num * num * math.pi, '6f')
m = format(num * num * 2.000000, '6f')
print(k, m, sep='\n')
# print(m)