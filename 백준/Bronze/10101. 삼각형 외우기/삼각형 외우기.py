#세 각의 크기가 모두 60이면, Equilateral
#세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
#세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
#세 각의 합이 180이 아닌 경우에는 Error

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == 60 and num2 == 60 and num3 == 60:
    print("Equilateral")
elif num1+num2+num3 == 180:
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Isosceles")
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print("Scalene")
elif num1+num2+num3 != 180:
    print("Error")
