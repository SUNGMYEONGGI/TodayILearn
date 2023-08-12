n = list(map(int, input().split()))
scale_list = [1,2,3,4,5,6,7,8]

if n == scale_list:
    print('ascending')
elif n == scale_list[::-1]:
    print('descending')
else:
    print('mixed')