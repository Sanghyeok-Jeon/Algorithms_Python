totalDeposit = 0
deposit = 5
for bottle in map(int, input().split()):
    totalDeposit += deposit * bottle

print(totalDeposit)