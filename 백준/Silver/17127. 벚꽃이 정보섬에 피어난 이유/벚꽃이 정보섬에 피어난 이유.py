N = int(input())
A = list(map(int, input().split()))

answer = 0
multiple_i = 1
for i in range(0, N - 3):
    multiple_i *= A[i]

    multiple_j = 1
    for j in range(i + 1, N -2):
        multiple_j *= A[j]

        multiple_k = 1
        for k in range(j + 1, N - 1):
            multiple_k *= A[k]

            multiple_l = 1
            for l in range(k + 1, N):
                multiple_l *= A[l]

            answer = max(answer, multiple_i + multiple_j + multiple_k + multiple_l)

print(answer)
