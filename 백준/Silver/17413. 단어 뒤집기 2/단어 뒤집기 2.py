S = input()

i = 0
is_tag = False
tmp_word = ''
answer = ''
while i < len(S):
    if is_tag:
        if S[i] == '>':
            tmp_word += S[i]
            answer += tmp_word
            tmp_word = ''
            is_tag = False
        else:
            tmp_word += S[i]
    else:
        if S[i] == '<':
            answer += tmp_word[::-1]
            tmp_word = S[i]
            is_tag = True
        elif S[i] == ' ':
            answer += tmp_word[::-1] + ' '
            tmp_word = ''
        else:
            tmp_word += S[i]

    i += 1

answer += tmp_word[::-1]

print(answer)