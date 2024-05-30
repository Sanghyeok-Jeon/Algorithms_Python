A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = A * P
Y = B + D * (P-C) if P > C else B

print(X if X < Y else Y)