N = int(input())
trees = sorted(list(map(int, input().split())), reverse=True)

answer = 0
for i in range(N):
    answer = max(answer, trees[i] + (i + 1) + 1)

print(answer)