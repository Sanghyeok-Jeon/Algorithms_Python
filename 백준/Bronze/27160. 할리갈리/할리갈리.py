N = int(input())

dict_fruits = {}
for _ in range(N):
    fruit, num = input().split()

    if fruit in dict_fruits:
        dict_fruits[fruit] += int(num)
    else:
        dict_fruits[fruit] = int(num)

if 5 in dict_fruits.values():
    print('YES')
else:
    print('NO')