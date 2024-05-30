e, f, c = map(int, input().split())
totalEmpty = e + f
cnt = 0
while totalEmpty >= c:
    cnt += totalEmpty // c
    totalEmpty = totalEmpty // c + totalEmpty % c
print(cnt)