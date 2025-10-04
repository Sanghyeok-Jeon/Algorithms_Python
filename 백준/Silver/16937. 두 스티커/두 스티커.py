import sys
input = sys.stdin.readline

def can_place_stickers(h, w, s1, s2):
    r1, c1 = s1
    r2, c2 = s2

    return (
            (r1 + r2 <= h and max(c1, c2) <= w)
            or (r1 + r2 <= w and max(c1, c2) <= h)
            or (c1 + c2 <= h and max(r1, r2) <= w)
            or (c1 + c2 <= w and max(r1, r2) <= h)
            or (r1 + c2 <= h and max(c1, r2) <= w)
            or (r1 + c2 <= w and max(c1, r2) <= h)
            or (c1 + r2 <= h and max(r1, c2) <= w)
            or (c1 + r2 <= w and max(r1, c2) <= h)
            )

H, W = map(int, input().split())
N = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(N)]

max_area = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        S1 = stickers[i]
        S2 = stickers[j]

        if can_place_stickers(H, W, S1, S2):
            max_area = max(max_area, S1[0] * S1[1] + S2[0] * S2[1])

print(max_area)