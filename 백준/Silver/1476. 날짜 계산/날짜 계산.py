def find_year(E, S, M):
    year = 1
    while True:
        if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
            return year
        year += 1

E, S, M = map(int, input().split())

print(find_year(E, S, M))