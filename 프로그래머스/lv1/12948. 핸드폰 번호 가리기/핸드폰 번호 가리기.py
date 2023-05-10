def solution(phone_number):
    return str(len(phone_number[:-4]) * '*') + str(phone_number[-4:])