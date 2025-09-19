N = int(input())
people = list(range(1, N + 1))

index = 0
step = 1
while len(people) > 1:
    move = (step ** 3 - 1) % len(people)
    index = (index + move) % len(people)
    people.pop(index)
    step += 1

print(people[0])