V = int(input())
data = input()
A, B = 0, 0
for d in data:
    if d == 'A':
        A += 1
    else:
        B += 1

print('A' if A > B else 'Tie' if A == B else 'B')