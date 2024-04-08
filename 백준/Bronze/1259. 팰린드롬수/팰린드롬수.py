while True:
    num = input()
    cnt = 0
    
    if num == '0':
        break

    for i in range(len(num) // 2):
        if num[i] == num[-i-1]:
            continue
        elif num[i] != num[-i-1]:
            cnt += 1

    if cnt >= 1:
        print('no')
    elif cnt == 0:
        print('yes')