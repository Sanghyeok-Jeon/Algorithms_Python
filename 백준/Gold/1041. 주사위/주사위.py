N = int(input())
A, B, C, D, E, F = map(int, input().split())

total = 0
if N == 1:    # 제일 큰 값 빼고는 모두 노출됨
    total = A+B+C+D+E+F - max(A, B, C, D, E, F)
else:
    min1 = min(A, B, C, D, E, F)    # 한 면만 노출되는 경우
    min2 = min(A+B, A+C, A+D, A+E, B+C, B+D, B+F, C+E, C+F, D+E, D+F, E+F)    # 두 면이 노출되는 경우
    min3 = min(A+B+C, A+B+D, A+C+E, A+D+E, B+C+F, B+D+F, C+E+F, D+E+F)    # 세 면이 노출되는 경우

    total += ((N - 2) * (N - 2) * 5 + (N - 2) * 4) * min1    # 각 면 중앙 (N-2)*(N-2)*5개 + 1층 모서리 4*(N-2)개
    total += ((N - 2) * 8 + 4) * min2    # 1층 꼭지점 4개 + 1층이 아닌 모서리 8 * (N-2)개
    total += 4 * min3    # 1층이 아닌 꼭지점 4개

print(total)