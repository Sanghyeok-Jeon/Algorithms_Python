chess = [[0]*6 for _ in range(6)]
start = now = list(input())
chess[ord(start[0])-ord('A')][int(start[1])-1] = 1

possible = 1
for _ in range(35):
    tmp = list(input())
    tmp_sum = 0
    if 0 <= (ord(tmp[0])-ord('A')) < 6 and 0 <= int(tmp[1])-1 < 6:
        if abs(ord(now[0]) - ord(tmp[0])) and abs(int(now[1]) - int(tmp[1])):
            if abs(ord(now[0]) - ord(tmp[0])) + abs(int(now[1]) - int(tmp[1])) == 3:
                if not chess[ord(tmp[0])-ord('A')][int(tmp[1])-1]:
                    chess[ord(tmp[0])-ord('A')][int(tmp[1])-1] = 1
                    now = tmp
                else:
                    possible = 0
                    break
            else:
                possible = 0
                break
        else:
            possible = 0
            break
    else:
        possible = 0
        break

if abs(ord(now[0]) - ord(start[0])) + abs(int(now[1]) - int(start[1])) != 3:
    possible = 0

if possible:
    print('Valid')
else:
    print('Invalid')