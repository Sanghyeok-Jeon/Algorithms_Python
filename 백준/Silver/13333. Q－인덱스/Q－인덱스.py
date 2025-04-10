n = int(input())
thesis = sorted(list(map(int, input().split())), reverse=True)

q_index = 0
for k in range(n):
    if thesis[k] >= k + 1:
        q_index = k + 1
    else:
        break

print(q_index)