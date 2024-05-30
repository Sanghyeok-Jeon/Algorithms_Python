num = []
op = []
while True:
    data = input()
    if data == '=':
        result = num[0]
        for i in range(len(op)):
            if op[i] == '+':
                result = result + num[i+1]
            elif op[i] == '-':
                result = result - num[i+1]
            elif op[i] == '*':
                result = result * num[i+1]
            else:
                result = result // num[i+1]

        print(result)
        break
    elif data.isdigit():
        num.append(int(data))
    else:
        op.append(data)