def eratosthenes(n, k):
    numbers = [True] * (n + 1)
    count = 0

    for i in range(2, n + 1):
        if numbers[i]:
            # i의 배수를 지우기 시작
            for j in range(i, n + 1, i):
                if numbers[j]:
                    numbers[j] = False
                    count += 1
                    if count == k:
                        return j

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

print(eratosthenes(n, k))