s = input()
patterns = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
result = len(s)

for pattern in patterns:
    if pattern in s:
        cnt = s.count(pattern)
        s = s.replace(pattern, ' ' * len(pattern))
        result -= (len(pattern) - 1) * cnt

print(result)