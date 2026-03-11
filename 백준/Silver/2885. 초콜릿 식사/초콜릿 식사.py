import sys

K = int(sys.stdin.readline().strip())

N = 1
while N < K:
    N <<= 1

m = N.bit_length() - 1                 
tz = (K & -K).bit_length() - 1         
cuts = m - tz

print(N, cuts)