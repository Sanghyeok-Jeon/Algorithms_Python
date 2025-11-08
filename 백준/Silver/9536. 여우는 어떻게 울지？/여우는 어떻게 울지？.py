import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sounds = input().split()
    known = set()
    while True:
        info = input()
        if info.startswith("what does the fox say"):
            break
        _, _, noise = info.split()
        known.add(noise)
    result = [s for s in sounds if s not in known]
    
    print(" ".join(result))