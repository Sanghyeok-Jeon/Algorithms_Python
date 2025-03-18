T = int(input())
for i in range(1, T + 1):
    data = input()

    alpha = [0] * 26
    for d in data:
        if d.isalpha():
            alpha[ord(d.lower()) - ord('a')] += 1

    print('Case {}: '.format(i), end='')
    if min(alpha) == 0:
        print('Not a pangram')
    elif min(alpha) == 1:
        print('Pangram!')
    elif min(alpha) == 2:
        print('Double pangram!!')
    else:
        print('Triple pangram!!!')