def backtracking(m, tmp_lst, sel_num_lst):
    if m == N:
        print(*tmp_lst)
        return

    for i in range(1, N + 1):
        if not sel_num_lst[i]:
            sel_num_lst[i] = True
            backtracking(m+1, tmp_lst + [i], sel_num_lst)
            sel_num_lst[i] = False

N = int(input())
selected_num = [True] + [False] * N
backtracking(0, [], selected_num)