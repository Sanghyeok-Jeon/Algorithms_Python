A = int(input(), base=2)
B = int(input(), base=2)
N = 100_000
M = 2 ** N - 1

print(bin(A & B)[2:].zfill(N))
print(bin(A | B)[2:].zfill(N))
print(bin(A ^ B)[2:].zfill(N))
print(bin(A ^ M)[2:].zfill(N))
print(bin(B ^ M)[2:].zfill(N))