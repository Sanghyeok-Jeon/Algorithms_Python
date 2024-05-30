N = int(input())
mascot = input()
K = int(input())

if mascot == 'annyong':
    if K % 2:
        print(K)
    else:
        if K < N:
            print(K+1)
        else:
            print(K-1)
else:
    if K % 2:
        if K < N:
            print(K+1)
        else:
            print(K-1)
    else:
        print(K)