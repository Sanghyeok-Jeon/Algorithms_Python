N = int(input())
A, B = map(int, input().split())

print(N if A//2 + B > N else A//2 + B)