S, K, H = map(int, input().split())

if S + K + H >= 100:
    print('OK')
else:
    minScore = min(S, K, H)
    if minScore == S:
        print('Soongsil')
    elif minScore == K:
        print('Korea')
    else:
        print('Hanyang')