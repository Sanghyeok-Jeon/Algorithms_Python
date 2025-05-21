def is_hansu(number):
    if number < 100:
        return True

    digits = list(map(int, str(number)))
    return (digits[0] - digits[1]) == (digits[1] - digits[2])

def count_hansu(N):
    count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1
    return count

N = int(input())

print(count_hansu(N))