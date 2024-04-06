wood_data = list(map(int, input().split()))

while True:
    if wood_data == [1, 2, 3, 4, 5]:
        break
    for i in range(4):
        if wood_data[i] > wood_data[i+1]:
            wood_data[i], wood_data[i+1] = wood_data[i+1], wood_data[i]
            print(*wood_data)