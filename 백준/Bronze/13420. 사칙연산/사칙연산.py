T = int(input())
for _ in range(T):
    A, op, B, eq, C = input().split()

    if op == '+':
        if int(A) + int(B) == int(C):
            print('correct')
        else:
            print('wrong answer')
    elif op == '-':
        if int(A) - int(B) == int(C):
            print('correct')
        else:
            print('wrong answer')
    elif op == '*':
        if int(A) * int(B) == int(C):
            print('correct')
        else:
            print('wrong answer')
    else:
        if int(A) // int(B) == int(C):
            print('correct')
        else:
            print('wrong answer')