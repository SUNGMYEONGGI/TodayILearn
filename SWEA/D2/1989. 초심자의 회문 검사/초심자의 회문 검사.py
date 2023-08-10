n = int(input())
cnt = 1
for _ in range(n):
    s = input()
    s1 = s[::-1]
    if s == s1:
        print(f'#{cnt} 1')
        cnt += 1
    else:
        print(f'#{cnt} 0')
        cnt += 1