N = input()

if len(N) == 1:
    print(1)
elif int(N) >= int('1' * len(N)):
    print(len(N))
else:
    print(len(N) - 1)