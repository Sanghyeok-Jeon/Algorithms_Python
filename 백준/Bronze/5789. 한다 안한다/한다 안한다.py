N = int(input())
for _ in range(N):
    data = input()
    if data[len(data)//2] == data[len(data)//2 - 1]:
        print('Do-it')
    else:
        print('Do-it-Not')