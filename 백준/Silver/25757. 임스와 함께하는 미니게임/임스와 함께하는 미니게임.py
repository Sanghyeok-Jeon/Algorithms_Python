import sys
input = sys.stdin.readline

N, game = input().split()

player = set()
for _ in range(int(N)):
    player.add(input())

if game == 'Y':
    print(len(player))
elif game == 'F':
    print(len(player) // 2)
else:
    print(len(player) // 3)