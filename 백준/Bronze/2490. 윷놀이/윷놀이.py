for _ in range(3):
    data = list(map(int, input().split()))
    zero = data.count(0)
    one = data.count(1)
    
    if zero == 1 and one == 3:
        print('A')
    elif zero == 2 and one == 2:
        print('B')
    elif zero == 3 and one == 1:
        print('C')
    elif zero == 4:
        print('D')
    else:
        print('E')
