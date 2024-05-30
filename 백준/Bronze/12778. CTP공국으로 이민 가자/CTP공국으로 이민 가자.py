T = int(input())
for _ in range(T):
    M, mode = input().split()
    target = list(input().split())
    
    answer = []
    if mode == 'C':
        for t in target:
            answer.append(ord(t) - ord('A') + 1)
    else:
        for t in target:
            answer.append(chr(int(t) + ord('A') - 1))
    
    print(*answer)