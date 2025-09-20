N = int(input())

answer = N - 1
for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        answer = N - N // i
        break

print(answer)