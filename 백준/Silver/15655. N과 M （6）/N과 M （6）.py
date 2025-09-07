def backtracking(start, tmp_lst):
    if len(tmp_lst) == M:
        print(*tmp_lst)
        return

    for i in range(start, N):
        backtracking(i + 1, tmp_lst + [nums[i]])

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

backtracking(0, [])