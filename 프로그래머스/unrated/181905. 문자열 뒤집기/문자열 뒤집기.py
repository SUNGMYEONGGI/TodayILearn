def solution(my_string, s, e):
    sent = my_string[s:e+1][::-1]
    return my_string[:s] + sent + my_string[e+1:]