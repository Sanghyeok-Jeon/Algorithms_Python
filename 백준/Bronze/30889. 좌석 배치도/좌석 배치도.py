N = int(input())
seat = [['.'] * 20 for _ in range(10)]
for _ in range(N):
    seat_no = input()
    seat[ord(seat_no[0]) - ord('A')][int(seat_no[1:]) - 1] = 'o'

for i in range(10):
    print(''.join(seat[i]))