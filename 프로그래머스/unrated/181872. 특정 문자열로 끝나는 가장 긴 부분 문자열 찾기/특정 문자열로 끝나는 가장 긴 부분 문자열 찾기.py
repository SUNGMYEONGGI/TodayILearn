def solution(mystring, pat):
    answer = ''
    if mystring.endswith(pat) == True:
        return mystring
    else:
        for i in range(len(mystring)):
            mystring = mystring.rstrip(mystring[-1:])
            if mystring.endswith(pat) == True:
                return mystring