word = 'WelcomeToSMUPC'

N = int(input())
print(word[N % len(word) - 1])