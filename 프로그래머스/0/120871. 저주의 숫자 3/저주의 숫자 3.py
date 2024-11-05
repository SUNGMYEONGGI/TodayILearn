def solution(n):
    cnt = 0
    for i in range(1,n+1):
        cnt += 1
        
        if cnt % 3 == 0 and '3' in str(cnt):
            cnt += 1
            while True:
                if '3' not in str(cnt):
                    break
                if '3' in str(cnt):
                    cnt += 1
        elif cnt % 3 == 0:
            cnt += 1
            while True:
                if '3' not in str(cnt):
                    break
                if '3' in str(cnt):
                    cnt += 1
        elif cnt % 3 != 0:
            if '3' in str(cnt):
                cnt += 1
                if cnt % 3 == 0:
                    cnt += 1
        print(f'10진법 {i}의 3x 마을에서 쓰는 숫자는 {cnt}입니다.')
    return cnt