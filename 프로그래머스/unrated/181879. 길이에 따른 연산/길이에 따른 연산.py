def solution(num_list):
    result_sum = 0
    result_mul = 1
    
    if len(num_list) >= 11:
        for i in num_list:
            result_sum += i
        return result_sum
    
    elif len(num_list) <= 10:
        for i in num_list:
            result_mul *= i
        return result_mul