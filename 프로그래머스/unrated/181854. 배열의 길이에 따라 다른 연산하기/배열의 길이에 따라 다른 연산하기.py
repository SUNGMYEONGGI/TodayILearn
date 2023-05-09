def solution(arr, n):
    answer_even = []
    answer_odd = []
    
    if len(arr) % 2 != 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer_odd.append(arr[i] + n)
            elif i % 2 != 0:
                answer_odd.append(arr[i])
        return answer_odd 
    
    if len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer_even.append(arr[i])
            elif i % 2 != 0:
                answer_even.append(arr[i]+ n)
        return answer_even
        