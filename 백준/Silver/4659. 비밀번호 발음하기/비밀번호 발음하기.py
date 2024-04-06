# 1. 모음 존재를 확인
# 2. 모음과 자음이 3개 연속으로 오면 안됨
# 3. 같은 문자가 2개 이상오면 안되고 'ee', 'oo'는 허용

while True:
    password = input()
    if password == 'end':
        break
    
    stop_point = 0
    lencnt = 0 # 1번 조건 password len개수만큼 채우면
    Mcnt = 0 # 모음개수
    Jcnt = 0 # 자음개수
    lentemp = ''
    
    for i in range(0, len(password)):
        if password[i] in ('a', 'e', 'i', 'o', 'u'):
            Mcnt += 1
            Jcnt = 0
            # print(password[i], Jcnt)
            if Mcnt == 3:
                break
            if lentemp != password[i]:
                lentemp = password[i]
            elif lentemp == password[i]:
                if lentemp + password[i] == 'ee' or lentemp + password[i] == 'oo':
                    stop_point -= 1
                stop_point += 1
                break
        elif password[i] not in ('a', 'e', 'i', 'o', 'u'):
            lencnt += 1
            Jcnt += 1
            Mcnt = 0
            # print(password[i], Jcnt)
            if lencnt == len(password):
                break
            if lentemp != password[i]:
                lentemp = password[i]
            elif lentemp == password[i]:
                stop_point += 1
                break
            if Jcnt == 3:
                break

    if Mcnt == 3 or Jcnt == 3:
        print(f'<{password}> is not acceptable.')
    elif stop_point == 1:
        print(f'<{password}> is not acceptable.')
    elif lencnt == len(password):
        print(f'<{password}> is not acceptable.')
    else:
        print(f'<{password}> is acceptable.')