s = input()
count0 = 0
count1 = 0

if s[0] == '0':
    count0 += 1
elif s[0] == '1':
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count0 += 1
            # print(count0)
        elif s[i+1] == '1':
            count1 += 1
            # print(count1)
    else:
        continue

print(min(count0, count1))