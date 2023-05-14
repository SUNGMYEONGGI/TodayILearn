def solution(num_list):
    list_add = 0
    list_mul = 1
    
    for i in num_list:
        list_add += i
    list_add *= list_add
    for j in num_list:
        list_mul *= j
        
    if list_add > list_mul:
        return 1
    else:
        return 0