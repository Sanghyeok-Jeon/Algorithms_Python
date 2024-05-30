import sys

N = int(input())
nameFrontTwo = {}
for _ in range(N):
    name = sys.stdin.readline()[0]
    if name in nameFrontTwo:
        nameFrontTwo[name] += 1
    else:
        nameFrontTwo[name] = 1

result = []
for k, v in nameFrontTwo.items():
    if v >= 5:
        result.append(k)

if result:
    print(''.join(sorted(result)))
else:
    print('PREDAJA')