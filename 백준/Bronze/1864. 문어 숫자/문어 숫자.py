dataDict = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}
while True:
    data = input()
    if data == '#':
        break

    answer = 0
    N = len(data)
    for i in range(N):
        answer += dataDict[data[i]] * (8**(N-1-i))

    print(answer)