S = int(input())

answer = 0
for i in range(1, S + 1):
    if S - i < 0:
        break

    S -= i
    answer = i

print(answer)