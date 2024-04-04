data = [num for num in [int(input()) for i in range(7)] if num % 2 != 0]

if data:
    print(sum(data), min(data), sep='\n')
else:
    print(-1)