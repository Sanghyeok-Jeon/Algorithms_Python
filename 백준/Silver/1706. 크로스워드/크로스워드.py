def find_words(grid, r, c):
    words = []

    for i in range(r):
        word = ''
        for j in range(c):
            if grid[i][j]!= '#':
                word += grid[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)

    for j in range(c):
        word = ''
        for i in range(r):
            if grid[i][j]!= '#':
                word += grid[i][j]
            else:
                if len(word) >= 2:
                    words.append(word)
                word = ''
        if len(word) >= 2:
            words.append(word)

    return words

r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]

words = find_words(grid, r, c)
print(min(words))