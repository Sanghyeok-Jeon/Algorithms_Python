def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

def LCM(x, y):
    result = (x*y) // GCD(x, y)
    return result

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(LCM(A, B))