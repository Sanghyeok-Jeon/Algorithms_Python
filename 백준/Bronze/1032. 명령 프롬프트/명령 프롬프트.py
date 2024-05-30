N = int(input())
data = [input() for _ in range(N)]
l = len(data[0])
answer = ''

if N == 1:
    answer = data[0]
else:
    for i in range(l):
        target = ''
        for j in range(N):
            if j == 0:
                target += data[j][i]
            elif j == N-1:
                if target == data[j][i]:
                    answer += target
                else:
                    answer += '?'
            else:
                if target != data[j][i]:
                    answer += '?'
                    break

print(answer)