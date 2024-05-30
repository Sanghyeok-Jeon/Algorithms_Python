def GCD(x, y):
    while y:
        x, y = y, x%y
    return x

N = int(input())

tree = []
treeGap = []
for i in range(N):
    tree.append(int(input()))
    if i:
        treeGap.append(tree[i] - tree[i-1])

gcd = treeGap[0]
for i in range(1, N-1):
    gcd = GCD(gcd, treeGap[i])

print((tree[-1] - tree[0])//gcd - N + 1)