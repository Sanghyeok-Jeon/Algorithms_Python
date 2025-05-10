target = input()
N = int(input())

answer = 0
for _ in range(N):
    tmp_ring = input()
    tmp_ring += tmp_ring

    if target in tmp_ring:
        answer += 1

print(answer)