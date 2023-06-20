def solution(order):
    cnt = 0
    
    for i in order:
        if 'americano' in i:
            cnt += 4500
        elif 'latte' in i:
            cnt += 5000
        elif 'anything' in i:
            cnt += 4500
    return cnt