def solution(myString, pat):
    myStr = str.maketrans('AB', 'BA')
    myString = myString.translate(myStr)
    if pat in myString:
        return 1
    else:
        return 0