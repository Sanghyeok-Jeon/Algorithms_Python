N = int(input())
totalEvolution = 0
maxEvolution = 0
maxPokemon = ''
for _ in range(N):
    pokemon = input()
    needCandy, haveCandy = map(int, input().split())

    cntEvolution = 0
    while haveCandy >= needCandy:
        cntEvolution += 1
        haveCandy -= needCandy
        haveCandy += 2

    if cntEvolution > maxEvolution:
        maxEvolution = cntEvolution
        maxPokemon = pokemon

    totalEvolution += cntEvolution

print(totalEvolution)
print(maxPokemon)