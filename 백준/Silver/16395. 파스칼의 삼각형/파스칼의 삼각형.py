n, k = map(int, input().split())
pascal = [[0]*(n+1) for _ in range(n+1)]
for j in range(1, n+1):
    pascal[1][j] = 1

for i in range(2, n+1):
    for j in range(1, n+1):
        pascal[i][j] = pascal[i-1][j] + pascal[i][j-1]

print(pascal[n-k+1][k])