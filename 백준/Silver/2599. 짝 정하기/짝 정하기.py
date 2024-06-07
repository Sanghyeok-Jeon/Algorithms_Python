N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

possible = False
for i in range(0, A[0] + 1):
    ab = i
    ac = A[0] - ab
    bc = C[1] - ac
    ba = B[0] - bc
    ca = A[1] - ba
    cb = C[0] - ca

    if ab >= 0 and ac >= 0 and ba >= 0 and bc >= 0 and ca >= 0 and cb >= 0:
        print(1)
        print(ab, ac)
        print(ba, bc)
        print(ca, cb)
        possible = True
        break

if not possible:
    print(0)