import sys

N, M = map(int, sys.stdin.readline().split())
dicPokeNo = {}
dicPokeNm = {}

pokeNo = 1
for _ in range(N):
    pokeNm = sys.stdin.readline().rstrip()
    dicPokeNm[pokeNm] = pokeNo
    dicPokeNo[pokeNo] = pokeNm
    pokeNo += 1

for _ in range(M):
    problem = sys.stdin.readline().rstrip()

    try:
        print(dicPokeNo[int(problem)])
    except:
        print(dicPokeNm[problem])