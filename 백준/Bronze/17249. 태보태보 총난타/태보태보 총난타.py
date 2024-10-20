S = input()
S_left = S[:S.index('(')]
S_right = S[S.index(')'):]

print(S_left.count('@'), S_right.count('@'))