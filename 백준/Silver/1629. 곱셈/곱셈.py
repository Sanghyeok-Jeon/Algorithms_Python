def DivideAndConquer(a, b):
    if b == 1:
        return a % C

    tmpDAC = DivideAndConquer(a, b//2)
    if b % 2:
        return tmpDAC * tmpDAC * a % C
    else:
        return tmpDAC * tmpDAC % C

A, B, C = map(int, input().split())

print(DivideAndConquer(A, B))