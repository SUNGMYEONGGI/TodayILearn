words = input()
dialog = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
answer = 0

for i in words:
    for j in dialog:
        if i in j:
            answer += dialog.index(j)+3

print(answer)