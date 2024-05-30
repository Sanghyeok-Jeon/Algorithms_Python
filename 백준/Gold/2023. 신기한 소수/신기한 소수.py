def PRIME(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

def DFS(n, l):
    if l == N:
        print(n)
        return

    for i in range(1, 10, 2):
        if PRIME(n * 10 + i):
            DFS(n * 10 + i, l+1)

N = int(input())

DFS(2, 1)
DFS(3, 1)
DFS(5, 1)
DFS(7, 1)