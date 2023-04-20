S = int(input())

for _ in range(S):
    num1, num2 = map(str, input().split())
    num2 = list(num2)
    answer = ''
    for i in range(len(num2)):
        answer += int(num1) * num2[i]
    print(answer)