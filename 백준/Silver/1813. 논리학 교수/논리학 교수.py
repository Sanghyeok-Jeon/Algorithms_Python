N = int(input())
data = list(map(int, input().split()))
dict_num = {0:0}

for num in data:
    if num in dict_num:
        dict_num[num] += 1
    else:
        dict_num[num] = 1

max_num = -1
for key, value in dict_num.items():
    if key == value:
        max_num = max(max_num, key)

print(max_num)