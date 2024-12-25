answer = 0
for i in range(3):
    tmp = input()
    if tmp.isnumeric():
        tmp_num = int(tmp)
        answer = tmp_num + (3 - i)

if answer % 3 == 0 and answer % 5 == 0:
    print('FizzBuzz')
elif answer % 3 == 0 and answer % 5 != 0:
    print('Fizz')
elif answer % 3 != 0 and answer % 5 == 0:
    print('Buzz')
else:
    print(answer)