import sys

N = int(input())
M = int(input())
S = input()

ans = 0
cnt = 0
i = 0

while i < M-2:
    if S[i] == "I" and S[i+1] == "O" and S[i+2] == "I":
        cnt += 1
        if cnt == N:
            cnt -= 1
            ans += 1
        i += 1
    else:
        cnt = 0
    i += 1

print(ans)