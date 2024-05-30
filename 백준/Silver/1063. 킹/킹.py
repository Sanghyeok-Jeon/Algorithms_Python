import sys

k, s, n = sys.stdin.readline().split()
King = [ord(k[0])-ord('A')+1, int(k[1])]
stone = [ord(s[0])-ord('A')+1, int(s[1])]
N = int(n)
move = [input() for _ in range(N)]

for i in range(N):
    if move[i] == 'R':
        if King[0]+1 < 9:
            if King[0]+1 == stone[0] and King[1] == stone[1]:
                if stone[0]+1 < 9:
                    King[0] += 1
                    stone[0] += 1
                else:
                    continue
            else:
                King[0] += 1
        else:
            continue

    elif move[i] == 'L':
        if King[0]-1 > 0:
            if King[0]-1 == stone[0] and King[1] == stone[1]:
                if stone[0]-1 > 0:
                    King[0] -= 1
                    stone[0] -= 1
                else:
                    continue
            else:
                King[0] -= 1
        else:
            continue

    elif move[i] == 'B':
        if King[1]-1 > 0:
            if King[0] == stone[0] and King[1]-1 == stone[1]:
                if stone[1]-1 > 0:
                    King[1] -= 1
                    stone[1] -= 1
                else:
                    continue
            else:
                King[1] -= 1
        else:
            continue

    elif move[i] == 'T':
        if King[1]+1 < 9:
            if King[0] == stone[0] and King[1]+1 == stone[1]:
                if stone[1]+1 < 9:
                    King[1] += 1
                    stone[1] += 1
                else:
                    continue
            else:
                King[1] += 1
        else:
            continue

    elif move[i] == 'RT':
        if King[0]+1 < 9 and King[1]+1 < 9:
            if King[0]+1 == stone[0] and King[1]+1 == stone[1]:
                if stone[0] + 1 < 9 and stone[1] + 1 < 9:
                    King[0] += 1
                    King[1] += 1
                    stone[0] += 1
                    stone[1] += 1
                else:
                    continue
            else:
                King[0] += 1
                King[1] += 1
        else:
            continue

    elif move[i] == 'LT':
        if King[0]-1 > 0 and King[1]+1 < 9:
            if King[0]-1 == stone[0] and King[1]+1 == stone[1]:
                if stone[0]-1 > 0 and stone[1]+1 < 9:
                    King[0] -= 1
                    King[1] += 1
                    stone[0] -= 1
                    stone[1] += 1
                else:
                    continue
            else:
                King[0] -= 1
                King[1] += 1
        else:
            continue

    elif move[i] == 'RB':
        if King[0]+1 < 9 and King[1]-1 > 0:
            if King[0]+1 == stone[0] and King[1]-1 == stone[1]:
                if stone[0]+1 < 9 and stone[1]-1 > 0:
                    King[0] += 1
                    King[1] -= 1
                    stone[0] += 1
                    stone[1] -= 1
                else:
                    continue
            else:
                King[0] += 1
                King[1] -= 1
        else:
            continue

    elif move[i] == 'LB':
        if King[0]-1 > 0 and King[1]-1 > 0:
            if King[0]-1 == stone[0] and King[1]-1 == stone[1]:
                if stone[0]-1 > 0 and stone[1]-1 > 0:
                    King[0] -= 1
                    King[1] -= 1
                    stone[0] -= 1
                    stone[1] -= 1
                else:
                    continue
            else:
                King[0] -= 1
                King[1] -= 1
        else:
            continue

lastKing = chr(ord('A')+King[0]-1) + str(King[1])
lastStone = chr(ord('A')+stone[0]-1) + str(stone[1])

print(lastKing)
print(lastStone)