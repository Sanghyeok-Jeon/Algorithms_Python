T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    answer = sum(n for n in range(1, 2 * A // B + 1, 2))

    print(answer)