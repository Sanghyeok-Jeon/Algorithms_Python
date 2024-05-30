import sys
import collections

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    P = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    numbers = sys.stdin.readline().rstrip()[1:-1].split(',')
    X = collections.deque()
    for number in numbers:
        if number.isdigit():
            X.append(number)

    reverseCheck = 1
    flagError = False
    for p in P:
        if p == 'R':
            reverseCheck *= -1
        else:
            if len(X):
                if reverseCheck == 1:
                    X.popleft()
                else:
                    X.pop()
            else:
                flagError = True
                break

    if flagError:
        print('error')
    else:
        if reverseCheck == -1:
            X.reverse()
        print('[' + ','.join(list(map(str, X))) + ']')
