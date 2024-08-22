N = int(input())

claps = 0
for num in range(1, N + 1):
    str_n = str(num)
    claps += str_n.count('3') + str_n.count('6') + str_n.count('9')

print(claps)