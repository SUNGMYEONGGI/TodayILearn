N = input()
data = ''

for i in N:
    if i.isupper() == True:
        data += i.lower()
    elif i.islower() == True:
        data += i.upper()
        
print(data)