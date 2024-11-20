S = input()
K = input()

new_S = ''
for s in S:
    if s.isalpha():
        new_S += s

if K in new_S:
    print(1)
else:
    print(0)