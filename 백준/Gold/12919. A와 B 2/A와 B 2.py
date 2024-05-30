from collections import deque

s = input()
t = input()

n = len(s)
q = deque()
q.append(t)

# T를 변형하여 S와 비교
answer = 0
while q:
    tmp = q.popleft()

    if tmp == s:
        answer = 1
        break
    elif len(tmp) < n:
        break

    if tmp[0] == 'B':    # T의 맨앞이 B인 경우, 맨앞을 제외하고 뒤집는다.
        q.append(tmp[1:][::-1])

    if tmp[-1] == 'A':    # T의 맨뒤가 A인 경우, 맨뒤를 제외한다.
        q.append(tmp[:-1])

print(answer)