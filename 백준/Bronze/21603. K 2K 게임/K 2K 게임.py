N, K = map(int, input().split())
f_k = K % 10
f_2k = (2 * K) % 10

arr_x = []
for x in range(1, N+1):
    f_x = x % 10
    if f_x != f_k and f_x != f_2k:
        arr_x.append(x)

print(len(arr_x))
print(*arr_x)