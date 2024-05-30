Cu, Du = map(int, input().split())
Cd, Dd = map(int, input().split())
Cp, Dp = map(int, input().split())
H = int(input())

time = 0
H -= Du + Dd + Dp
for i in range(1, H + 1):
    if H <= 0:
        break

    if not i % Cu:
        H -= Du

    if not i % Cd:
        H -= Dd

    if not i % Cp:
        H -= Dp

    time += 1

print(time)