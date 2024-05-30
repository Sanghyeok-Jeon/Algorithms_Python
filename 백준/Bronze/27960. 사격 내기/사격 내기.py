A, B = map(int, input().split())
print(int(bin(A ^ B)[2:], 2))