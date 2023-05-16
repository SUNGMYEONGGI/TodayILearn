K = int(input())
count = 0
    
if K % 5 == 0:
    print(K // 5)
    
else:
    while K >= 0:
        if K % 5 != 0:
            K -= 3
            count += 1
            if K % 5 == 0:
                count += (K // 5)
                print(count)
                break
    else:
        print(-1)