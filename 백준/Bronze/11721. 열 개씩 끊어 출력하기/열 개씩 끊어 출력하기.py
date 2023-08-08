s = input()
cnt = 0
data = ''

for i in s:
    data += i
    cnt += 1
    if cnt % 10 == 0:
        print(data)
        cnt = 0
        data = ''
        
print(data)