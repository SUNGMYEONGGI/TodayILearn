N = int(input())

for _ in range(N):
    score = list(input())
    result, answer = 0, 1
    
    for i in score:
        if i == 'O':
            result += answer
            answer += 1
        elif i == 'X':
            answer = 1
    print(result)