X = input()
print(int(X[2:],16) if X[1]=='x' else int(X[1:],8) if X[0]=='0' else X)