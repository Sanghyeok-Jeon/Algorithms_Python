N = int(input())
words = [input() for _ in range(N)]
unique = []

for word in words:
    is_new = True
    for u in unique:
        if len(word) != len(u):
            continue

        if word in (u * 2):
            is_new = False
            break

    if is_new:
        unique.append(word)

print(len(unique))