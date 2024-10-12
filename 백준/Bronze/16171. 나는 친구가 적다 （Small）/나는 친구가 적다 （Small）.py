S = input()
K = input()

new_S = ''.join(char for char in S if not char.isnumeric())

if K in new_S:
    print(1)
else:
    print(0)