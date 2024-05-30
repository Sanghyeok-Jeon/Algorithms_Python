N = int(input())

answer = 0
for i in range(1, int(N**0.5)+1):
    if not N % i:
        if i * i == N:
            answer += 1
        else:
            answer += 2

print(answer)