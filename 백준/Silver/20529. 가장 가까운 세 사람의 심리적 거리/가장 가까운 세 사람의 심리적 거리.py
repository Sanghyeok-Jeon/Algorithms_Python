from itertools import combinations

T = int(input())
for _ in range(T):
    N = int(input())
    data = input().split()
    combData = combinations(data, 3)

    ans = float('inf')
    if N > 32:
        print(0)
    else:
        for mbti in combData:
            ans = min(ans, len(set(mbti[0])-set(mbti[1])) + len(set(mbti[1])-set(mbti[2])) + len(set(mbti[2])-set(mbti[0])))
        print(ans)