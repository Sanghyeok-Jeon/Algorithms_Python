def check_numbers(cnt, used_list, str_num):
    if cnt == k:
        possible_set.add(str_num)
        return

    cnt += 1

    for j in range(n):
        if not used_list[j]:
            used_list[j] = True
            check_numbers(cnt, used_list, str_num + str(numbers[j]))
            used_list[j] = False

n = int(input())
k = int(input())
numbers = [int(input()) for _ in range(n)]
possible_set = set()
used = [False] * n

for i in range(n):
    used[i] = True
    check_numbers(1, used, str(numbers[i]))
    used[i] = False

print(len(possible_set))