import math

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    answer = 0

    for i in range(1, len(data) - 1):
        for j in range(i + 1, len(data)):
            answer += math.gcd(data[i], data[j])

    print(answer)