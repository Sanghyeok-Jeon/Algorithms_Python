import sys
input = sys.stdin.readline

N = int(input())
rainbowDance = set()
for _ in range(N):
    A, B = input().split()
    if A == 'ChongChong' or B == 'ChongChong' or A in rainbowDance or B in rainbowDance:
        rainbowDance.add(A)
        rainbowDance.add(B)

print(len(rainbowDance))