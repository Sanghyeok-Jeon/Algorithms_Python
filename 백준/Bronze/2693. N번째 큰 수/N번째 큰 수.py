T = int(input())
for _ in range(T):
    A = sorted(list(map(int, input().split())), reverse=True)
    print(A[2])