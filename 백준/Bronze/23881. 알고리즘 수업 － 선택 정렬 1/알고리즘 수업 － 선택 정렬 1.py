def selection_sort(N):
    cnt_chg = 0
    for i in range(N - 1, 0, -1):
        last = i
        for j in range(i - 1, -1, -1):
            if A[j] > A[last]:
                last = j

        if i != last:
            A[i], A[last] = A[last], A[i]
            cnt_chg += 1

        if cnt_chg == K:
            return (print(A[last], A[i]))

    return (print(-1))

N, K = map(int, input().split())
A = list(map(int, input().split()))

selection_sort(N)