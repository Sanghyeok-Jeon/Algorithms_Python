S = input()
for s in S:
    tmp = str(ord(s))
    tmp_sum = sum(map(int, tmp))
    
    print(s * tmp_sum)