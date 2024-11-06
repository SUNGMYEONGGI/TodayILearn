def solution(s, n):
    answer = ""
    
    for i in s:
        if i == " ":
            answer += " "
            continue
            
        ascii_num = ord(i)
        if i.isupper() == True:
            if 91 <= ascii_num+n:
                answer += chr((ascii_num + n - 26))
            else:
                answer += chr(ascii_num + n)
        elif i.islower() == True: 
            if 123 <= ascii_num+n:
                answer += chr((ascii_num + n - 26))
            else:
                answer += chr(ascii_num + n)
    return answer