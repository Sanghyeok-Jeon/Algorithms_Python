max_num = 0
result = ''
for _ in range(7):
    seminar, num = input().split()
    if int(num) > max_num:
        max_num = int(num)
        result = seminar

print(result)