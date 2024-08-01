import sys
input = sys.stdin.readline

S1, S2 = map(int, input().split())

answer = 'Accepted'
for _ in range(S1):
    sample_answer, my_answer = map(int, input().split())
    if sample_answer != my_answer:
        answer = 'Wrong Answer'
        break

if answer != 'Wrong Answer':
    for _ in range(S2):
        system_answer, my_answer = map(int, input().split())
        if system_answer != my_answer:
            answer = 'Why Wrong!!!'
            break

print(answer)