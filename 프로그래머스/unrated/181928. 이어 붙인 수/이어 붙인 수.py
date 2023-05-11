def solution(num_list):
    list1 = []
    list2 = []
    answer1 = ''
    answer2 = ''
    for i in num_list:
        if i % 2 == 0:
            list1.append(i)
        elif i % 2 != 0:
            list2.append(i)
    
    for j in list1:
        answer1 += str(j)
    for k in list2:
        answer2 += str(k)
    
    return int(answer1)+int(answer2)