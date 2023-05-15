K = int(input())
price = 1000 - K
Yen_list = [500, 100, 50, 10, 5, 1]
result = 0

for yen in Yen_list:
    result += price // yen
    price %= yen

print(result)