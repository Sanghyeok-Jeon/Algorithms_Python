AB = input()

if len(AB) == 2:
    print(int(AB[0]) + int(AB[1]))
elif len(AB) == 3:
    if AB[1] == '0':
        print(int(AB[:2]) + int(AB[2]))
    else:
        print(int(AB[0]) + int(AB[1:]))
else:
    print(20)