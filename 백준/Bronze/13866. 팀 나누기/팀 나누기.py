A, B, C, D = map(int, input().split())
data = sorted([A, B, C, D])

print(abs((data[0]+data[3])-(data[1]+data[2])))