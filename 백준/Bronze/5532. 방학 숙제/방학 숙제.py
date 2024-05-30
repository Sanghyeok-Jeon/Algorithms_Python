L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

finishMath = A//C + 1 if A%C else A//C
finishKorean = B//D + 1 if B%D else B//D
freeDay = L - finishMath if finishMath > finishKorean else L - finishKorean

print(freeDay)