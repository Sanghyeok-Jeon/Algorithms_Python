S = input()
N = len(S)
answer = ''

i = 0
while i < len(S):
    if S[i] in ['a', 'e', 'i', 'o', 'u']:
        answer += S[i]
        i += 3
    else:
        answer += S[i]
        i += 1

print(answer)