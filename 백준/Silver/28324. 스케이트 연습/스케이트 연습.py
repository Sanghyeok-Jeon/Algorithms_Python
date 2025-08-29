N = int(input())
V = list(map(int, input().split()))

V[N - 1] = 1
answer = V[N - 1]
if N != 1:
    for i in range(N - 2, -1, -1):
        if V[i] > V[i + 1]:
            new_V = min(V[i + 1] + 1, V[i])
            V[i] = new_V

        answer += V[i]

print(answer)