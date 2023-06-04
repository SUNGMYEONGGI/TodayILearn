A, B = map(int, input().split())

def gcd(A, B):
    if A % B == 0:
        return B
    else:
        return gcd(B, A % B)

def lcm(A, B):
    return (A * B) // gcd(A, B)
    
print(gcd(A, B))
print(lcm(A, B))