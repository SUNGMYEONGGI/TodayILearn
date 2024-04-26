import sys

n = int(sys.stdin.readline())
data = []
stack = []
cnt = 0

for _ in range(n):
    data.append(sys.stdin.readline().rstrip())
    if len(data[0]) % 2 == 0:
        for text in data[0]:
            for i in range(0, len(text[0])):
                stack.append(text[i])
                # print(stack)
                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        # print(stack)
        if len(stack) == 0:
            cnt += 1
        data, stack = [], []
    else:
        data, stack = [], []
        continue

print(cnt)