N = int(input())

def fibonacci(N, fb_list):
    for i in range(N):
        fb_list.append(fb_list[-1] + fb_list[-2])

    return fb_list[N]

print(fibonacci(N, [0, 1]))