R, C = map(int, input().split())
design = [list(input()) for _ in range(R)]
A, B = map(int, input().split())

for d in design:
    d.extend(d[::-1])

addDesign = []
for d in reversed(design):
    addDesign.append(list(d))

design.extend(addDesign)

if design[A-1][B-1] == '#':
    design[A-1][B-1] = '.'
else:
    design[A-1][B-1] = '#'

for d in design:
    print(''.join(d))