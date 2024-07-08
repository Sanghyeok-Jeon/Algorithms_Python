N = int(input())
door_open = int(input())

if N > 5:
    print('Love is open door')
else:
    for i in range(2, N + 1):
        door_open = int(not door_open)
        print(door_open)