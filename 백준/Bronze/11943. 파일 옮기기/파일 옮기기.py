A, B = map(int, input().split())
C, D = map(int, input().split())

way1 = A + D
way2 = B + C

print(way1 if way1 < way2 else way2)