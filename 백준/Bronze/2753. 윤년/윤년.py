IntYear = int(input())

if (IntYear % 4 == 0 and IntYear % 100 != 0 or IntYear % 400 == 0):
	print("1")
else:
	print("0")