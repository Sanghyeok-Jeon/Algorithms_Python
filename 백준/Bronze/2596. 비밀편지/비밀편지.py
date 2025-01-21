secret_key = {'A': '000000',
                 'B': '001111',
                 'C': '010011',
                 'D': '011100',
                 'E': '100110',
                 'F': '101001',
                 'G': '110101',
                 'H': '111010'}

N = int(input())
secret_letter = input()

answer = ''
word_num = 1
for i in range(0, N * 6, 6):
    flag_find = False
    for key, value in secret_key.items():
        if bin(int(secret_letter[i:i + 6], 2) ^ int(value, 2))[2:].count('1') < 2:
            answer += key
            flag_find = True
            break

    if not flag_find:
        print(word_num)
        exit(0)

    word_num += 1

print(answer)