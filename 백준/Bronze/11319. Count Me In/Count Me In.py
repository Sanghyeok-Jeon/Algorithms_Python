v_letters = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

S = int(input())
for _ in range(S):
    sentence = input()
    consonants, vowels = 0, 0

    for char in sentence:
        if char.isalpha():
            if char in v_letters:
                vowels += 1
            else:
                consonants += 1

    print(consonants, vowels)