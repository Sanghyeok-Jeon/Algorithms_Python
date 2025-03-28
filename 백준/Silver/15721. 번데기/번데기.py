A = int(input())
T = int(input())
BD = int(input())

cnt_B = 0
cnt_D = 0

n = 0
list_speak_BD = []
while True:
    n += 1

    for _ in range(2):
        cnt_B += 1
        list_speak_BD.append((cnt_B, 0))
        cnt_D += 1
        list_speak_BD.append((cnt_D, 1))

    for _ in range(n + 1):
        cnt_B += 1
        list_speak_BD.append((cnt_B, 0))

    for _ in range(n + 1):
        cnt_D += 1
        list_speak_BD.append((cnt_D, 1))

    if cnt_B >= T:
        print(list_speak_BD.index((T, BD)) % A)
        break