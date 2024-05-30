N, B = map(int, input().split())

newNum = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = ''
while N:
    answer += newNum[N % B]
    N //= B

print(answer[::-1])