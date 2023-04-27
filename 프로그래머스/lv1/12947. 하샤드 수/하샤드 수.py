def solution(x):
    answer = []
    add_arr = 0
    str_x = str(x)
    
    for i in str_x:
        a = int(i)
        answer.append(a)
        
    for j in answer:
        add_arr += j
        
    if x % add_arr == 0:
        return True
    elif add_arr == 1:
        if x % (add_arr+1) == 0:
            return True
    else:
        return False