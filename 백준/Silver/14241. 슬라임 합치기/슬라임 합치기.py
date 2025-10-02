N = int(input())
slimes = list(map(int, input().split()))

score = 0
while len(slimes) > 1:
    slimes.sort()
    a = slimes.pop()
    b = slimes.pop()
    score += a * b
    slimes.append(a + b)

print(score)