origin = 1000
pay = int(input())
change = origin - pay

coin = 0

coin += change // 500
change = change % 500

coin += change // 100
change = change % 100

coin += change // 50
change = change % 50

coin += change // 10
change = change % 10

coin += change // 5
change = change % 5

coin += change

print(coin)