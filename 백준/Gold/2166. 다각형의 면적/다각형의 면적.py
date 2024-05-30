import sys
input = sys.stdin.readline

N = int(input())
vertex = []
for _ in range(N):
    vertex.append(list(map(int, input().split())))
vertex.append(vertex[0])    # 첫번째 꼭지점을 한 번 더 추가

xy, yx = 0, 0
for i in range(N):
    xy += vertex[i][0] * vertex[i+1][1]    # 각 꼭지점의 x좌표를 다음 꼭지점 좌표의 y값과 곱함
    yx += vertex[i][1] * vertex[i+1][0]    # 각 꼭지점의 y좌표 값을 다음 x좌표 값들과 곱함

print(round(abs((xy - yx) / 2), 1))