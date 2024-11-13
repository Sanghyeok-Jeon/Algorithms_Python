S = list(input())
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    tmp = S[B]
    S[B] = S[A]
    S[A] = tmp

print(''.join(S))