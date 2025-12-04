import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = {input().strip() for _ in range(n)}

for _ in range(m):
    memo = input().strip().split(',')
    keywords.difference_update(memo)
    print(len(keywords))