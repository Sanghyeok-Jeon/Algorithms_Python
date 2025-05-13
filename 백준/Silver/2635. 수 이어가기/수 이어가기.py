def generate_sequence(first, second):
    sequence = [first, second]
    while True:
        next_number = sequence[-2] - sequence[-1]
        if next_number < 0:
            break
        sequence.append(next_number)
    return sequence

def find_longest_sequence(N):
    longest_sequence = []
    for second in range(N + 1):
        current_sequence = generate_sequence(N, second)
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
    return longest_sequence

N = int(input())

longest_sequence = find_longest_sequence(N)

print(len(longest_sequence))
print(*longest_sequence)