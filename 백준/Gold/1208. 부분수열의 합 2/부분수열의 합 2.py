import sys
from itertools import combinations
input = sys.stdin.readline

def calc_sum_comb_and_sort(array, sum_array):
    for i in range(len(array) + 1):
        for comb in combinations(array, i):
            sum_array.append(sum(comb))

    return sum_array

N, S = map(int, input().split())
data = list(map(int, input().split()))

# 왼쪽 수열, 오른쪽 수열 만들기
ldata, rdata = data[:N // 2], data[N // 2:]

# 왼쪽 수열의 부분 수열의 합
ldata_sum = calc_sum_comb_and_sort(ldata, [])
ldata_sum.sort()
len_lsum = len(ldata_sum)

# 오른쪽 수열의 부분 수열의 합
rdata_sum = calc_sum_comb_and_sort(rdata, [])
rdata_sum.sort(reverse=True)
len_rsum = len(rdata_sum)

result = 0

idx_ldata, idx_rdata = 0, 0
while idx_ldata < len_lsum and idx_rdata < len_rsum:
    ld, rd = ldata_sum[idx_ldata], rdata_sum[idx_rdata]
    sum_d = ld + rd

    if sum_d == S:    # 합이 S와 같은 경우
        cnt_ld, cnt_rd = 1, 1
        idx_ldata += 1
        idx_rdata += 1
        # 같은 값 존재하는지 확인
        while idx_ldata < len_lsum and ldata_sum[idx_ldata] == ld:
            cnt_ld += 1
            idx_ldata += 1
        while idx_rdata < len_rsum and rdata_sum[idx_rdata] == rd:
            cnt_rd += 1
            idx_rdata += 1

        result += cnt_ld * cnt_rd

    elif sum_d > S:    # 합이 S보다 큰 경우
        idx_rdata += 1
    else:    # 합이 S보다 작은 경우
        idx_ldata += 1

if S == 0:    # 공집합 제거
    result -= 1
print(result)