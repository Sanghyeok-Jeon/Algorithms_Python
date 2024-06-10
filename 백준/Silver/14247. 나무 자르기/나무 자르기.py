import sys
input = sys.stdin.readline

n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

# 나무를 자라는 속도에 따라 정렬 (자라는 속도가 빠른 나무부터 자르기)
trees = sorted(zip(H, A), key=lambda x: x[1])

# 구할 수 있는 최대 양
total_cost = 0
for i in range(n):
    total_cost += trees[i][0] + trees[i][1] * i

print(total_cost)