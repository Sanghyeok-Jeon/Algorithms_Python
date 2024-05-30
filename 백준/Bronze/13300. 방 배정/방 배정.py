N, K = map(int, input().split())

girl = [0] * 7
boy = [0] * 7
room = 0

for _ in range(N):
    S, Y = map(int, input().split())
    if S:
        boy[Y] += 1
    else:
        girl[Y] += 1

for b in boy:
    room += b//K + 1 if b % K else b//K

for g in girl:
    room += g//K + 1 if g % K else g//K

print(room)