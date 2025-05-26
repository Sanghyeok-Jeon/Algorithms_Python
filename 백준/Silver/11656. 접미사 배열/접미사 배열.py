S = input()

suffix = [S[i:] for i in range(len(S))]
suffix.sort()

for i in range(len(suffix)):
    print(suffix[i])