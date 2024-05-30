word = [input() for _ in range(6)]
possible = 0

for i in range(6):
    for j in range(6):
        if i == j:
            continue
        for k in range(6):
            if j == k or k == i:
                continue
            result = [word[i], word[j], word[k]]
            result.append(word[i][0] + word[j][0] + word[k][0])
            result.append(word[i][1] + word[j][1] + word[k][1])
            result.append(word[i][2] + word[j][2] + word[k][2])
            result.sort()
            if result == word:
                possible = 1
                print(word[i])
                print(word[j])
                print(word[k])
                break
        if possible:
            break
    if possible:
        break

if not possible:
    print(0)