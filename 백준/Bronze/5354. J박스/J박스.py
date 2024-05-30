T = int(input())
for tc in range(T):
    N = int(input())
    for i in range(N):
        if i == 0 or i == N-1:
            print('#'*N)
        else:
            print('#{}#'.format('J'*(N-2)))
    print()