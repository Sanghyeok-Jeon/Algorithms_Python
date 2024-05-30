N = int(input())
name = input()

scoreName = 0
for n in name:
    scoreName += ord(n) - ord('A') + 1

print(scoreName)