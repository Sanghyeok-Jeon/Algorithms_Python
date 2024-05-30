def DFS(n, temp):
    global maxResult, minResult, N

    if n == N-1:
        if temp > maxResult:
            maxResult = temp
        if temp < minResult:
            minResult = temp
        return

    if calc[0]:
        calc[0] -= 1
        DFS(n + 1, temp + num[n + 1])
        calc[0] += 1
    if calc[1]:
        calc[1] -= 1
        DFS(n + 1, temp - num[n + 1])
        calc[1] += 1
    if calc[2]:
        calc[2] -= 1
        DFS(n + 1, temp * num[n + 1])
        calc[2] += 1
    if calc[3]:
        calc[3] -= 1
        DFS(n + 1, -(-temp // num[n + 1]) if temp < 0 else temp // num[n + 1])
        calc[3] += 1
        
N = int(input())
num = list(map(int, input().split()))
calc = list(map(int, input().split()))

maxResult = -1000000000
minResult = 1000000000

DFS(0, num[0])

print(maxResult)
print(minResult)