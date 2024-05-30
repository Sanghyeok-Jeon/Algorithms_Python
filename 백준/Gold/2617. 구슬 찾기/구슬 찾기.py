def cntBigger(n):
    visited[n] = 1
    cnt = 0
    for b in bigger[n]:
        if visited[b]:
            continue
        cnt += 1
        cnt += cntBigger(b)
    return cnt

def cntSmaller(n):
    visited[n] = 1
    cnt = 0
    for s in smaller[n]:
        if visited[s]:
            continue
        cnt += 1
        cnt += cntSmaller(s)
    return cnt

N, M = map(int, input().split())
smaller = [[] for _ in range(N+1)]
bigger = [[] for _ in range(N+1)]
for _ in range(M):
    big, small = map(int, input().split())
    smaller[big].append(small)
    bigger[small].append(big)

MID = (N+1) // 2
result = 0
for i in range(1, N+1):
    visited = [0] * (N+1)
    if MID <= cntBigger(i) or MID <= cntSmaller(i):
        result += 1

print(result)
