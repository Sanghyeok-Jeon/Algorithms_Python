T = int(input())
for _ in range(T):
    A, B = input().split()
    print(bin(int(A, 2) + int(B, 2))[2:])