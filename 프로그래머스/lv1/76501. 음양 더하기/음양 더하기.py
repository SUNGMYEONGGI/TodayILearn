def solution(absolutes, signs):
    answer = []
    result = 0
    a = len(absolutes)
    print(a)
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            absolutes[i] = abs(absolutes[i])
            answer.append(absolutes[i])
        elif signs[i] == False:
            absolutes[i] *= -1 
            answer.append(absolutes[i])
    for j in answer:
        result += j
        
    return result
    
    