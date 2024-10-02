N = input()

if '7' not in N and int(N) % 7:
    print(0)
elif '7' not in N and not int(N) % 7:
    print(1)
elif '7' in N and int(N) % 7:
    print(2)
else:
    print(3)