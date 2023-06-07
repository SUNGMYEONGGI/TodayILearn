x_data = []
y_data = []

for _ in range(3):
    x, y = map(int, input().split())
    x_data.append(x)
    y_data.append(y)
    
for i in range(3):
    if x_data.count(x_data[i]) == 1:
        x4 = x_data[i]
    elif y_data.count(y_data[i]) == 1:
        y4 = y_data[i]
        
print(x4, y4)