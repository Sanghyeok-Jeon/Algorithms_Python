N = int(input())

new_num = ''
for i in range(1, N + 1):
    new_num += str(i)

print(new_num.index(str(N)) + 1)