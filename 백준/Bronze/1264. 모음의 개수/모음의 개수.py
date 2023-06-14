while True:
    a = input()
    cnt = 0
    if a == '#':
        break
    for i in a:
        if i in ['i', 'e', 'a', 'o', 'u', 'I', 'A', 'E', 'O', 'U']:
            cnt += 1
    
    print(cnt)