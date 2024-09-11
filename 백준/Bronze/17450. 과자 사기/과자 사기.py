price_s, weight_s = map(int, input().split())
sum_weight_s = weight_s * 10
sum_price_s = price_s * 10 if price_s * 10 < 5000 else price_s * 10 - 500
S = sum_weight_s / sum_price_s

price_n, weight_n = map(int, input().split())
sum_weight_n = weight_n * 10
sum_price_n = price_n * 10 if price_n * 10 < 5000 else price_n * 10 - 500
N = sum_weight_n / sum_price_n

price_u, weight_u = map(int, input().split())
sum_weight_u = weight_u * 10
sum_price_u = price_u * 10 if price_u * 10 < 5000 else price_u * 10 - 500
U = sum_weight_u / sum_price_u

if S == max(S, N, U):
    print('S')
elif N == max(S, N, U):
    print('N')
else:
    print('U')