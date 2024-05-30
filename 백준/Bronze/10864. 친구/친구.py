N, M = map(int, input().split())
friends = [set() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    friends[A].add(B)
    friends[B].add(A)
    
for i in range(1, N+1):
    print(len(friends[i]))