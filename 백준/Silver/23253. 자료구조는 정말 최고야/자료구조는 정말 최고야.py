import sys
input = sys.stdin.readline

N, M = map(int, input().split())
for _ in range(M):
    k = int(input())
    pile_book = list(map(int, input().split()))

    if pile_book != sorted(pile_book, reverse=True):
        print('No')
        exit(0)

print('Yes')