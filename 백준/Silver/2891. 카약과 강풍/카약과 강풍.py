N, S, R = map(int, input().split())
list_broken = list(map(int, input().split()))
list_spare = list(map(int, input().split()))

list_cnt_kayak = [0] * (N + 1)
for i in range(1, N + 1):
    if i in list_spare and i in list_broken:
        list_cnt_kayak[i] = 1
    elif i in list_spare:
        list_cnt_kayak[i] = 2
    elif i in list_broken:
        list_cnt_kayak[i] = 0
    else:
        list_cnt_kayak[i] = 1

for i in range(1, N + 1):
    if list_cnt_kayak[i] == 0:
        if i == 1:
            if list_cnt_kayak[i + 1] == 2:
                list_cnt_kayak[i + 1] -= 1
                list_cnt_kayak[i] += 1
        elif i == N:
            if list_cnt_kayak[i - 1] == 2:
                list_cnt_kayak[i - 1] -= 1
                list_cnt_kayak[i] += 1
        else:
            if list_cnt_kayak[i - 1] == 2:
                list_cnt_kayak[i - 1] -= 1
                list_cnt_kayak[i] += 1
            elif list_cnt_kayak[i + 1] == 2:
                list_cnt_kayak[i + 1] -= 1
                list_cnt_kayak[i] += 1

print(list_cnt_kayak[1:].count(0))