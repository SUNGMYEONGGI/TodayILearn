# (->10cm ( 쌓이면 5cm씩
# () -> 20cm

dish = list(input())
number = 0

for i in range(1, len(dish)):
    if dish[i] == '(':
        if dish[i-1] == '(':
            number += 5
        elif dish[i-1] == ')':
            number += 10
    elif dish[i] == ')':
        if dish[i-1] == '(':
            number += 10
        elif dish[i-1] == ')':
            number += 5
print(number+10)