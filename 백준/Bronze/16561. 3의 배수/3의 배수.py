n = int(input())
if n < 9:
    print(0)
else:
    answer = 1
    cnt = 2
    for i in range(9, n, 3):
        answer += cnt
        cnt += 1
    print(answer)