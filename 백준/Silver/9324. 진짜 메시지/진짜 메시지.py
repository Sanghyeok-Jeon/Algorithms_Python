T = int(input())
for _ in range(T):
    s = input()
    count = [0] * 26
    i = 0
    real = True
    while i < len(s):
        idx = ord(s[i]) - ord('A')
        count[idx] += 1
        if count[idx] == 3:
            if i + 1 >= len(s) or s[i + 1] != s[i]:
                real = False
                break
            count[idx] = 0  
            i += 1
        i += 1
    print("OK" if real else "FAKE")
