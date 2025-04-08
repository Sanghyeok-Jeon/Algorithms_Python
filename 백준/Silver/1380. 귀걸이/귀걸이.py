scenario = 0
while True:
    scenario += 1
    n = int(input())
    if n == 0:
        break

    student = [''] + [input() for _ in range(1, n + 1)]

    earrings = []
    for _ in range(2 * n - 1):
        num, alpha = input().split()
        int_num = int(num)
        if int_num in earrings:
            earrings.remove(int_num)
        else:
            earrings.append(int_num)

    print(scenario, student[earrings[0]])