N, M = map(int, input().split())

double_origin = []
for _ in range(N):
    origin = input()
    tmp = ''
    for o in origin:
        tmp += o + o

    double_origin.append(tmp)

is_same = True
for i in range(N):
    target = input()
    if double_origin[i] != target:
        is_same = False

if is_same:
    print('Eyfa')
else:
    print('Not Eyfa')