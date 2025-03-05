N = int(input())
data = [input() for _ in range(N)]

M = int(input())
candidate = [input() for _ in range(M)]

target_start = ''
target_end = ''
for i in range(N):
    if data[i] == '?':
        if i > 0:
            target_start = data[i - 1][-1]

        if i < N - 1:
            target_end = data[i + 1][0]

answer = ''
for cd in candidate:
    if target_start == '' and target_end == '':
        if cd not in data:
            answer = cd
            break
    elif target_start == '':
        if cd[-1] == target_end and cd not in data:
            answer = cd
            break
    elif target_end == '':
        if cd[0] == target_start and cd not in data:
            answer = cd
            break
    else:
        if cd[0] == target_start and cd[-1] == target_end and cd not in data:
            answer = cd
            break

print(answer)