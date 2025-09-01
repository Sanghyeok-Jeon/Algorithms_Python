N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
arr_need_cnt = []

for i in range(N):
    cnt = 0
    for j in range(arr[i], arr[i] + 5):
        if j not in arr:
            cnt += 1

    arr_need_cnt.append(cnt)

print(min(arr_need_cnt))