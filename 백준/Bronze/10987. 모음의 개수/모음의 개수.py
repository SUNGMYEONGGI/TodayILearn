cnt = 0
sent = input()
for i in sent:
    if i in 'aeiou':
        cnt += 1

print(cnt)