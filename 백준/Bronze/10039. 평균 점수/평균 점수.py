score = []
sum = 0

for _ in range(5):
    student = int(input())
    score.append(student)

for i in range(len(score)):
    if score[i] <= 39:
        score[i] = 40
    else:
        continue
        
for j in score:
    sum += j

print(sum//5)