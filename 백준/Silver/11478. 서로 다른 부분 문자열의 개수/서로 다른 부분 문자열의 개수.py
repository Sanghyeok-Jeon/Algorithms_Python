S = input()

subset = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        subset.add(S[i:j+1])

print(len(subset))