N = int(input())

answer = ''

for i in range(N//2):
    answer += '1 2 '

if N % 2:
    answer += '3'

print(answer)