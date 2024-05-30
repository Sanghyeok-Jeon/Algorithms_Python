N = int(input())
data = []
for _ in range(N):
    title, diff = input().split()
    data.append([title, int(diff)])

print(sorted(data, key=lambda x:x[1])[0][0])