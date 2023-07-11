def solution(numbers):
    sent = ''
    result = ''
    for i in numbers:
        sent += i
        if sent == "zero":
            result += '0'
            sent = ''
        elif sent == "one":
            result += '1'
            sent = ''
        elif sent == "two":
            result += '2'
            sent = ''
        elif sent == "three":
            result += '3'
            sent = ''
        elif sent == "four":
            result += '4'
            sent = ''
        elif sent == "five":
            result += '5'
            sent = ''
        elif sent == "six":
            result += '6'
            sent = ''
        elif sent == "seven":
            result += '7'
            sent = ''
        elif sent == "eight":
            result += '8'
            sent = ''
        elif sent == "nine":
            result += '9'
            sent = ''
                        
    return int(result)