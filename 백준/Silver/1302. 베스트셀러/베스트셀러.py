N = int(input())
books = {}
for _ in range(N):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_cnt = 0
max_book = ''
for k, v in books.items():
    if v > max_cnt:
        max_book = k
        max_cnt = v
    elif v == max_cnt:
        max_book = min(max_book, k)

print(max_book)