N = int(input())
prime = [0, 0] + [1] * 999
A = [1]

for i in range(2, 1001):
    if prime[i]:
        if len(A) != N:
            A.append(i)
        else:
            break
        for j in range(2*i, 1001, i):
            prime[j] = 0

print(N)
print(*A)