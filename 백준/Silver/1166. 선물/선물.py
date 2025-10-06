N, L, W, H = map(int, input().split())

left, right = 0, min(L, W, H)
for _ in range(100):
    mid = (left + right) / 2
    if (L // mid) * (W // mid) * (H // mid) >= N:
        left = mid
    else:
        right = mid

print('{:.10f}'.format(left))