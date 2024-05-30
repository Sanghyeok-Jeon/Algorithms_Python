N = int(input())
listNumber = [int(input()) for _ in range(N)]
listNumber.sort()
for n in listNumber:
    print(n)