n = int(input())

for _ in range(n):
    sent = list(input())
    tmp = sent[0].upper()
    sent[0] = tmp
    
    print(''.join(sent))