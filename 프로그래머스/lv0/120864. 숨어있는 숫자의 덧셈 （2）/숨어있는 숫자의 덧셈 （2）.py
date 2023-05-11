def solution(my_string):
    result = 0
    
    for i in range(65, 91):
        my_string = my_string.replace(chr(i), ' ')
    for j in range(97, 123):
        my_string = my_string.replace(chr(j), ' ')
    my_string = ((my_string.strip()).split(' '))
    sample_list = ' '.join(my_string).split()
    
    for k in sample_list:
        result += int(k)
    return result