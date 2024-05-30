N, W, H, L = map(int, input().split())
possible = (W//L) * (H//L)
print(min(N, possible))