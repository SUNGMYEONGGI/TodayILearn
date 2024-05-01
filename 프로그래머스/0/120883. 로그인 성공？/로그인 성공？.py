def solution(id_pw, db):
    cnt = 0
    answer = ''
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                answer = 'login'
                break
            elif i[1] != id_pw[1]:
                if answer == 'login':
                    continue
                else: answer = 'wrong pw'
        elif i[0] != id_pw[0]:
            cnt += 1
            if cnt == 3:
                answer = 'fail'
                
    return answer