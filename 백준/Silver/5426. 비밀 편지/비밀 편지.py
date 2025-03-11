T = int(input())
for _ in range(T):
    text_cipher = input()
    len_text_square = int(len(text_cipher) ** 0.5)
    text_plain = ''
    for i in range(len_text_square - 1, -1, -1):
        for j in range(len_text_square):
            text_plain += text_cipher[i + j * len_text_square]

    print(text_plain)