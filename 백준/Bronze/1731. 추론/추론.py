N = int(input())
sequence = [int(input()) for _ in range(N)]
    
is_arithmetic = True if (sequence[2]-sequence[1]) == (sequence[1]-sequence[0]) else False
    
if is_arithmetic:
    print(sequence[-1] + sequence[-1] - sequence[-2])
else:
    print(sequence[-1]*(sequence[-1]//sequence[-2]))