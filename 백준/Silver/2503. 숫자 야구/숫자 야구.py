def is_possible(number, guess, strike, ball):
    number = str(number)
    guess = str(guess)

    strike_count = sum(1 for a, b in zip(number, guess) if a == b)
    ball_count = sum(1 for a in number if a in guess) - strike_count

    return strike_count == strike and ball_count == ball

def baseball_game(questions):
    possible_numbers = []

    for number in range(123, 988):
        number_str = str(number)

        if len(set(number_str)) != 3 or '0' in number_str:
            continue

        if all(is_possible(number, guess, strike, ball) for guess, strike, ball in questions):
            possible_numbers.append(number)

    return len(possible_numbers)

n = int(input())
questions = [tuple(map(int, input().split())) for _ in range(n)]

result = baseball_game(questions)
print(result)
