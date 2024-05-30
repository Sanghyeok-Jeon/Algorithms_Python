N, L, D = map(int, input().split())
song = ('1'*L + '0'*5) * (N-1) + '1'*L
minTime = 0
while minTime < len(song):
    if song[minTime] == '0':
        break
    minTime += D
print(minTime)