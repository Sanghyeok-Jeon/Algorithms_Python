import sys
input = sys.stdin.readline

def rotations(seq):
    L = len(seq)
    return [tuple(seq[i:] + seq[:i]) for i in range(L)]

n = int(input().strip())
sample = list(map(int, input().split()))
m = int(input().strip())

candidates = [list(map(int, input().split())) for _ in range(m)]

rev = {1: 3, 3: 1, 2: 4, 4: 2}

patterns = set()

for r in rotations(sample):
    patterns.add(r)

reversed_sample = [rev[x] for x in sample][::-1]
for r in rotations(reversed_sample):
    patterns.add(r)

answers = []
for cand in candidates:
    if tuple(cand) in patterns:
        answers.append(cand)

print(len(answers))
for arr in answers:
    print(*arr)