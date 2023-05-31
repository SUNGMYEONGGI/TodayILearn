T = int(input())
MoneyList = [25, 10, 5, 1]

for _ in range(T):
    Quarter, Dime, Nickel, Penny = 0, 0, 0,0 
    c = int(input())
    Quarter += c // MoneyList[0]
    c %= MoneyList[0]
    # print('Quarter 이후 c의 값: ', c)
    Dime += c // MoneyList[1]
    c %= MoneyList[1]
    # print('Dime 이후 c의 값: ', c)
    Nickel += c // MoneyList[2]
    c %= MoneyList[2]
    # print('Nickel 이후 c의 값: ', c)
    Penny += c // MoneyList[3]
    c %= MoneyList[3]
    # print('Penny 이후 c의 값: ', c)
    print(Quarter, Dime, Nickel, Penny)