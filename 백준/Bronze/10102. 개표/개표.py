N = int(input())
voting = list(input())
vot_A = 0
vot_B = 0

for i in voting:
    if i == 'A':
        vot_A += 1
    elif i == 'B':
        vot_B += 1

if vot_A > vot_B:
    print('A')
elif vot_A < vot_B:
    print('B')
else:
    print('Tie')