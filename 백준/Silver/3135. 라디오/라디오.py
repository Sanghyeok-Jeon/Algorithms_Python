A, B = map(int, input().split())
N = int(input())
bookmark = []
for _ in range(N):
    bookmark.append(int(input()))

bookmark_selected = 0
diff_hz = abs(A - B)
for i in range(N):
    tmp_diff = abs(B - bookmark[i])
    if tmp_diff < diff_hz:
        diff_hz = tmp_diff
        bookmark_selected = bookmark[i]

print(diff_hz + 1 if bookmark_selected else diff_hz)