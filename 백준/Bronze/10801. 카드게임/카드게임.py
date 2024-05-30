scoreA = list(map(int, input().split()))
scoreB = list(map(int, input().split()))

winner = []
for i in range(10):
    if scoreA[i] > scoreB[i]:
        winner.append('A')
    elif scoreA[i] < scoreB[i]:
        winner.append('B')
    else:
        winner.append('D')

if winner.count('A') > winner.count('B'):
    print('A')
elif winner.count('A') < winner.count('B'):
    print('B')
else:
    print('D')