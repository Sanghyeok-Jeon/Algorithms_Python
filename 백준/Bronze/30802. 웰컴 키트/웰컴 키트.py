N = int(input())
tshirts = list(map(int, input().split()))
T, P = map(int, input().split())

order_t = 0
for ts in tshirts:
    order_t += ts // T + (1 if ts % T else 0)

order_p_bundle = N // P
order_p_each = N % P

print(order_t)
print(order_p_bundle, order_p_each)