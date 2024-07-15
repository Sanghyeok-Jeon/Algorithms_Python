T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(sum(n for n in range(1, 2 * A // B + 1, 2)))