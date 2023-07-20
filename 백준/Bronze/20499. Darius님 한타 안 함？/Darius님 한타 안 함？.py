kda = input()
kda = kda.split('/')
ka = int(kda[0])+int(kda[2])

if ka < int(kda[1]) or int(kda[1]) == 0:
    print('hasu')
else:
    print('gosu')