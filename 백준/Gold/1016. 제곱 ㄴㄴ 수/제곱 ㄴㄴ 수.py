min_num, max_num = map(int, input().split())

sieve_Eratosthenes = [False] * ((max_num - min_num) + 1)
count = max_num - min_num + 1    # 범위 내의 모든 수를 제곱 ㄴㄴ 수라고 가정.

square = 2    # 2부터 max_num 제곱근까지 반복
while square * square <= max_num:
    start = square * square
    i = min_num // start

    while start * i <= max_num:
        idx = start * i - min_num

        if idx >= 0 and not sieve_Eratosthenes[idx]:
            sieve_Eratosthenes[idx] = True
            count -= 1

        i += 1

    square += 1

print(count)