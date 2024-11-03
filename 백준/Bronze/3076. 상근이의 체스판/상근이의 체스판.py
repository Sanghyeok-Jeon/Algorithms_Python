R, C = map(int, input().split())
A, B = map(int, input().split())

for r in range(R):
    for _ in range(A):
        for c in range(C):
            print('.' * B if (r + c) % 2 else 'X' * B, end='')
        print()