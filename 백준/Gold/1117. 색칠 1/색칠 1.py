W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
total = W * H
paint = (x2 - x1) * (y2 - y1)

after_fold_w = f if f <= W // 2 else W - f
fold_y_cnt = c + 1

coloring = 0
if after_fold_w <= x1:
    coloring = paint * fold_y_cnt
elif x2 <= after_fold_w:
    coloring = paint * 2 * fold_y_cnt
else:
    coloring = (paint + (after_fold_w - x1) * (y2 - y1)) * fold_y_cnt

print(total - coloring)