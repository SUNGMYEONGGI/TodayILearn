N = int(input())

for _ in range(N):
    k = input().split()
    answer = float(k[0])
    
    for i in range(1, len(k)):
        if k[i] == '@':
            answer *= 3
        elif k[i] == '%':
            answer += 5
        elif k[i] == '#':
            answer -= 7
    print(f"{answer:.2f}")