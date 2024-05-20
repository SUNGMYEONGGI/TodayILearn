def solution(A,B):
    answer = 0 # 답
    temp = 0 # 임시 숫자
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer = temp + (A[i]*B[i])
        temp = answer
    
    return answer   