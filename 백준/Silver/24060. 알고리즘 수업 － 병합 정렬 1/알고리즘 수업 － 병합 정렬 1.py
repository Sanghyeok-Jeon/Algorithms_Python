import sys

def Merge_sort(A, p, r):
    if p < r and cnt <= K:
        q = (p + r) // 2
        Merge_sort(A, p, q)
        Merge_sort(A, q + 1, r)
        Merge(A, p, q, r)

def Merge(A, p, q, r):
    global cnt, ans
    i, j = p, q+1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i, t = p, 0
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            ans = A[i]
            break
        i += 1
        t += 1

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
cnt = 0
ans = -1
Merge_sort(A, 0, N-1)
print(ans)