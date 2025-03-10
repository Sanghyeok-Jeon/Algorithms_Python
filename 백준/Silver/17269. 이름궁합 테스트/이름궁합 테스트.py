def compatibility_score(name1, name2):
    stroke_values = {
        'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3,
        'G': 1, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1,
        'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
        'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2,
        'Y': 2, 'Z': 1
    }

    combined = ''.join(a + b for a, b in zip(name1, name2)) + name1[len(name2):] + name2[len(name1):]

    numbers = [stroke_values[char] for char in combined]

    # 궁합 점수 계산
    while len(numbers) > 2:
        numbers = [(numbers[i] + numbers[i + 1]) % 10 for i in range(len(numbers) - 1)]

    return numbers[0] * 10 + numbers[1]

N, M = map(int, input().split())
name1, name2 = input().split()

print('{}%'.format(compatibility_score(name1, name2)))
