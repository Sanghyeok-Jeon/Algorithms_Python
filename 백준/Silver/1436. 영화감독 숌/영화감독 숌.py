N = int(input())
movieName = 666
cnt = 0
while True:
    if '666' in str(movieName):
        cnt += 1
    if cnt == N:
        print(movieName)
        break
    movieName += 1