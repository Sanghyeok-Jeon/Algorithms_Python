N = int(input())
classNo = [list(map(int, input().split())) for _ in range(N)]
cntSameClass = [0] * N

for n in range(N):
    sameClass = [0] * N
    for grade in range(5):
        for studentNo in range(N):
            if studentNo != n and classNo[studentNo][grade] == classNo[n][grade]:
                sameClass[studentNo] = 1
    cntSameClass[n] = sum(sameClass)

print(cntSameClass.index(max(cntSameClass)) + 1)