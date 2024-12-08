N = int(input())
seat = input()

count_LL = seat.count('LL')

if count_LL <= 1:
    print(N)
else:
    print(N - count_LL + 1)