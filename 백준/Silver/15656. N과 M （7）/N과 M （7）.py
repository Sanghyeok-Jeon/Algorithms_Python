def backtracking(m, tmp_lst):
    if m == M:
        print(*tmp_lst)
        return

    for i in range(N):
        backtracking(m+1, tmp_lst + [nums[i]])


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
backtracking(0, [])