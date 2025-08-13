T = int(input())
for _ in range(T):
    n = int(input())
    primary_public_key = list(input().split())
    secondary_public_key = list(input().split())
    cryptogram = list(input().split())

    plaintext = [''] * n
    for i in range(n):
        plaintext[primary_public_key.index(secondary_public_key[i])] += cryptogram[i]

    print(*plaintext)