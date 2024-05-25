# 1. 물품을 구매할때 신청한 금액 전부 지원
# 2. d에는 물품의 금액이 들어있는 배열
# 3. 총 금액

def solution(d, budget):
    cnt = 0
    d.sort()
    for i in d:
        if budget >= i:
            budget -= i
            cnt += 1
            if budget == 0:
                return cnt
        elif budget < i:
            return cnt
    return cnt
    
    