while True:
    name, age, weight = input().split()

    if name == '#':
        break

    if int(age) >= 18 or int(weight) >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')