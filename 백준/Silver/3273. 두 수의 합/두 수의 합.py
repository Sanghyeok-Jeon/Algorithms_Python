n = int(input())
a = list(map(int, input().split()))
x = int(input())

answer = 0
a.sort()
i = 0
j = n - 1
while i < j:
    tmp_x = a[i] + a[j]
    if tmp_x == x:
        answer += 1
        i += 1
        j -= 1
    elif tmp_x > x:
        j -= 1
    else:
        i += 1

print(answer)