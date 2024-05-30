from collections import defaultdict

# 배열의 부분합을 구하는 함수
def get_partial_sums(arr):
    partial_sums = defaultdict(int)
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(i + 1, len_arr + 1):
            partial_sums[sum(arr[i:j])] += 1

    return partial_sums

# 두 배열의 합이 target이 되는 경우의 수를 구하는 함수
def count_target_sums(p_sum_A, p_sum_B, target):
    count = 0
    for num_A, freq_A in p_sum_A.items():
        count += freq_A * p_sum_B[target - num_A]

    return count

T = int(input())
n = int(input())
arr_A = list(map(int, input().split()))
m = int(input())
arr_B = list(map(int, input().split()))

# A 배열의 부분합
partial_sums_A = get_partial_sums(arr_A)

# B 배열의 부분합
partial_sums_B = get_partial_sums(arr_B)

# 목표 합이 되는 경우의 수
result = count_target_sums(partial_sums_A, partial_sums_B, T)

print(result)