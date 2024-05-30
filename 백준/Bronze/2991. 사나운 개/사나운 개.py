A, B, C, D = map(int, input().split())
PMN = list(map(int, input().split()))

for pmn in PMN:
    attacked = 0
    if 0 < pmn % (A+B) <= A:
        attacked += 1
    if 0 < pmn % (C+D) <= C:
        attacked += 1
    print(attacked)