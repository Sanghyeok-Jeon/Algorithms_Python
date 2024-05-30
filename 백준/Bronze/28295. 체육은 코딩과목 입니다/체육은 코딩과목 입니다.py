direction = ['N', 'E', 'S', 'W']

last_direction = 0
for _ in range(10):
    command = int(input())

    if command == 1:
        last_direction = (last_direction + 1) % 4
    elif command == 2:
        last_direction = (last_direction + 2) % 4
    else:
        last_direction = (last_direction - 1 if last_direction >= 1 else 3 - last_direction) % 4

print(direction[last_direction])