sing = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]

N = int(input())
answer = ''
if N % 14 in (3, 7, 11):
    tmp = 'tururu' + 'ru' * (N // 14)
    if tmp.count('ru') >= 5:
        answer = 'tu+ru*' + str(N // 14 + 2)
    else:
        answer = tmp
elif N % 14 in (4, 8, 12):
    tmp = 'turu' + 'ru' * (N // 14)
    if tmp.count('ru') >= 5:
        answer = 'tu+ru*' + str(N // 14 + 1)
    else:
        answer = tmp
else:
    answer = sing[N % 14 - 1]

print(answer)