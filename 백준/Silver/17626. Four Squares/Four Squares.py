import sys

n = int(sys.stdin.readline())
answer = 4
for i in range(int(n**0.5), int((n//4)**0.5), -1):
    if i * i == n:
        answer = 1
        break
    else:
        m = n - i*i
        for j in range(int(m**0.5), int((m//3)**0.5), -1):
            if i*i + j*j == n:
                answer = min(answer, 2)
            else:
                l = n - i*i - j*j
                for k in range(int(l**0.5), int((l//2)**0.5), -1):
                    if n == i*i + j*j + k*k:
                        answer = min(answer, 3)

print(answer)