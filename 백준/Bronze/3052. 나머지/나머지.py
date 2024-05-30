nameoji = []
for _ in range(10):
    N = int(input())
    if N % 42 not in nameoji:
        nameoji.append(N % 42)

print(len(nameoji))