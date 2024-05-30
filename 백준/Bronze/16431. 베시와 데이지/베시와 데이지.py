Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

moveB = max(abs(Br-Jr), abs(Bc-Jc))
moveD = abs(Dr-Jr) + abs(Dc-Jc)

print('bessie' if moveB < moveD else 'tie' if moveB == moveD else 'daisy')