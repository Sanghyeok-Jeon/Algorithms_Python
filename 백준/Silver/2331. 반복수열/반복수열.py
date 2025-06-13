def calculate_num(n, p):
    result = 0
    while n > 0:
        result += (n % 10) ** p
        n = n // 10
    return result

A, P = map(int, input().split())
list_origin = [A]

while True:
    D = calculate_num(list_origin[-1], P)
    if D in list_origin:
        break
    list_origin.append(D)

print(list_origin.index(D))