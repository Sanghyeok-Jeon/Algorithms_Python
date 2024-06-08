import sys
input = sys.stdin.readline

S = input()

answer = []
prev = ' '
i = 0
while i < len(S):
    c = S[i]

    if c in ('<', '>', '(', ')'):
        if prev == ' ':
            answer.append(c + ' ')
        else:
            answer.append(' ' + c + ' ')
        prev = ' '
    elif c in ('&', '|'):
        if prev == ' ':
            answer.append(c + c + ' ')
        else:
            answer.append(' ' + c + c + ' ')
        prev = ' '
        i += 1
    elif c == ' ':
        if prev != ' ':
            answer.append(' ')
        prev = ' '
    else:
        answer.append(c)
        prev = c

    i += 1

print(''.join(answer))