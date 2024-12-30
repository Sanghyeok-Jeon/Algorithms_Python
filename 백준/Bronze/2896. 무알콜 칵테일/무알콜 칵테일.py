A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

max_cnt = min(A / I, B / J, C / K)

print(A - I * max_cnt, B - J * max_cnt, C - K * max_cnt)