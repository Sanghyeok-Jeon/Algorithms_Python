n = int(input())

answer = set()
for i in range(1, int(n**0.5)+1):
    for j in range(1, n+1):
        if i * j <= n:
            answer.add((i, j) if i < j else (j, i))
        
print(len(answer))