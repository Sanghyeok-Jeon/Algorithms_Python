import sys

for _ in range(3):
    S = sum(map(int, (sys.stdin.readline() for _ in range(int(sys.stdin.readline())))))

    if not S:
        print(0)
    else:
        print('+' if S > 0 else '-')