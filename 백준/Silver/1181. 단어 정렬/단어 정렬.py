N = int(input())
data = set()
for _ in range(N):
    d = input()
    data.add((d, len(d)))

dt = sorted(data, key=lambda x: (x[1], x[0]))

for d in dt:
    print(d[0])