S = input()
if len(S) > 2 and S[0] == S[-1] == '"':
    print(S[1:-1])
else:
    print('CE')