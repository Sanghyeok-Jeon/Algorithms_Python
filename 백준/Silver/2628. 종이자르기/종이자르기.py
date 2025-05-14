W, L = map(int, input().split())
N = int(input())

w_cut = [0]
l_cut = [0]
for _ in range(N):
    target, num = map(int, input().split())

    if target == 0:
        w_cut.append(num)
    else:
        l_cut.append(num)

w_cut.sort()
l_cut.sort()

w_cut.append(L)
l_cut.append(W)

lst_w = []
for i in range(1, len(w_cut)):
    lst_w.append(w_cut[i] - w_cut[i - 1])

lst_l = []
for i in range(1, len(l_cut)):
    lst_l.append(l_cut[i] - l_cut[i - 1])

lst_extent = []
for w in lst_w:
    for l in lst_l:
        lst_extent.append(w * l)

print(max(lst_extent))