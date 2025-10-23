N = int(input())

lst_coin_cnt = [0, 1, 1, 2, 2, 1, 2, 1] + [0] * (100000 - 7)
for i in range(8, 100001):
    lst_coin_cnt[i] = min(lst_coin_cnt[i - 1], lst_coin_cnt[i - 2], lst_coin_cnt[i - 5], lst_coin_cnt[i - 7]) + 1

print(lst_coin_cnt[N])