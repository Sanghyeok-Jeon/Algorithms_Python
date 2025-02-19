T = int(input())
for _ in range(T):
    k = int(input())
    words = [input() for _ in range(k)]

    answer = 0
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            tmp_words = words[i] + words[j]
            if tmp_words == tmp_words[::-1]:
                answer = tmp_words
                break

        if answer != 0:
            break

    print(answer)