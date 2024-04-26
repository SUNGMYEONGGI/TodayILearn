def solution(my_string):
    my_string = my_string.lower()
    alpha = []
    answer = [0] * 52
    
    for i in range(65, 91):
        alpha.append(chr(i))
    for i in range(97, 123):
        alpha.append(chr(i))
        
    print(alpha, len(alpha))
    for j in range(len(alpha)):
        if alpha[j] in my_string:
            answer[j] += 1
        else:
            continue
            
            
    return answer