import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    num_select = [0] + [int(input()) for _ in range(N)]

    visited = [False] * (N + 1)
    selected_num = 1
    answer = 0

    while not visited[selected_num]:
        visited[selected_num] = True
        if selected_num == N:
            print(answer)
            break

        selected_num = num_select[selected_num]
        answer += 1
    else:
        print(0)