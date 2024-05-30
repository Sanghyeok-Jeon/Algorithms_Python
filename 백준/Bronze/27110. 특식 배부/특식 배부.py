N = int(input())
A, B, C = map(int, input().split())

chicken = 0
chicken += A if A < N else N
chicken += B if B < N else N
chicken += C if C < N else N

print(chicken)