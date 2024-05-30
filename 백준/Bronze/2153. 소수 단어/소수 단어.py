def is_prime(num):
    for i in range(2, num):
        if not num % i:
            return False
    return True

strAlpha = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input()
num = 0
for w in word:
    num += strAlpha.index(w)
    
print('It is a prime word.' if is_prime(num) else 'It is not a prime word.')