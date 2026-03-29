import sys

input = sys.stdin.readline

S, P = map(int, input().split())
dna = input().strip()
need = list(map(int, input().split()))

count = [0, 0, 0, 0]  

def idx(ch):
    if ch == 'A':
        return 0
    elif ch == 'C':
        return 1
    elif ch == 'G':
        return 2
    else:
        return 3

for i in range(P):
    count[idx(dna[i])] += 1

def is_valid():
    for i in range(4):
        if count[i] < need[i]:
            return False
    return True

answer = 0

if is_valid():
    answer += 1

for i in range(P, S):
    count[idx(dna[i])] += 1           
    count[idx(dna[i - P])] -= 1       

    if is_valid():
        answer += 1

print(answer)