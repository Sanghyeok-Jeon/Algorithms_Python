N, Q = map(int, input().split())
B = [0] + [int(input()) for _ in range(N)]

for _ in range(Q):
    q = int(input())

    answer = 0
    for i in range(1, N + 1):
        q -= B[i]
        if q < 0:
            answer = i
            break

    print(answer)