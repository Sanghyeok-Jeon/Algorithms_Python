n = int(input())
height = 0
block = 0

while block <= n:
    block += 2 * height * height + 2 * height + 1
    height += 1

print(height - 1)
