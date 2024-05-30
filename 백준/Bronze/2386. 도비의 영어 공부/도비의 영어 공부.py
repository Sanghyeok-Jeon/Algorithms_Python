while True:
    problem = input()

    target = problem[0]
    if target == '#':
        break

    cntTarget = 0
    for i in range(2, len(problem)):
        if target == problem[i] or target.upper() == problem[i]:
            cntTarget += 1

    print(target, cntTarget)