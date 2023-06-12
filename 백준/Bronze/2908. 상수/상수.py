num1, num2 = input().split()

# num1_string = num1[::-1]
num1_reverse = ''.join(reversed(num1))
num2_reverse = ''.join(reversed(num2))
print(max(num1_reverse, num2_reverse))