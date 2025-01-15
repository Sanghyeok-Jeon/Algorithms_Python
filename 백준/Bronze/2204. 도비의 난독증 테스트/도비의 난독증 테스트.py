while True:
    n = int(input())
    if n == 0:
        break

    words = []
    for i in range(n):
        word = input()
        words.append([word, word.upper()])

    print(sorted(words, key=lambda x:x[1])[0][0])