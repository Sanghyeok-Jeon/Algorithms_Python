T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    oneLeg = M * 2 - N
    twoLeg = (N - oneLeg) // 2

    print(oneLeg, twoLeg)