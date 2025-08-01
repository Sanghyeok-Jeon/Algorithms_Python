N = int(input())

set_word = set()
for _ in range(N):
    word = ''.join(sorted(input()))

    set_word.add(word)

print(len(set_word))