N1, N2 = map(int, input().split())
ant1 = list(input())[::-1]
ant2 = list(input())
all_ant = ant1 + ant2
move = int(input())

for _ in range(move):
    idx = 0
    while idx < N1+N2-1:
        if all_ant[idx] in ant1 and all_ant[idx+1] in ant2:
            all_ant[idx], all_ant[idx+1] = all_ant[idx+1], all_ant[idx]
            idx += 2
        else:
            idx += 1

print(''.join(all_ant))