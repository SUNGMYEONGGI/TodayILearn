n1, n2 = map(str, input().split())

min_n1 = n1.maketrans('6', '5')
max_n1 = n1.maketrans('5', '6')
min_n2 = n2.maketrans('6', '5')
max_n2 = n2.maketrans('5', '6')

print(int(n1.translate(min_n1)) + int(n2.translate(min_n2)), int(n1.translate(max_n1)) + int(n2.translate(max_n2)))