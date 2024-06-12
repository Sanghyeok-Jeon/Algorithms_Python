T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    print(min(data), max(data))