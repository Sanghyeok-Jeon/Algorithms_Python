T = int(input())
result = ''
for _ in range(T):
    name = input()
    if 'S' in name:
        result = name
        break

print(result)