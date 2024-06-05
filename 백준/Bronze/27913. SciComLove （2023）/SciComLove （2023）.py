N, Q = map(int, input().split())
origin_str = 'SciComLove'
n_str = list('SciComLove' + 'SciComLove' * (N // 10))[:N]

cnt_upper = 0
for s in n_str:
    if s.isupper():
        cnt_upper += 1

for _ in range(Q):
    i = int(input()) - 1
    if n_str[i].isupper():
        n_str[i] = n_str[i].lower()
        cnt_upper -= 1
    else:
        n_str[i] = n_str[i].upper()
        cnt_upper += 1

    print(cnt_upper)