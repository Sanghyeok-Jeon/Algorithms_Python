N = int(input())
data = [input() for _ in range(N)]
for n in range(N):
    if data[n][::-1] in data:
        lenStr = len(data[n])
        print(lenStr, data[n][lenStr//2])
        break