A = input()
B = input()
phoneNumber = ''
for i in range(8):
    phoneNumber += A[i]
    phoneNumber += B[i]

while len(phoneNumber) > 2:
    tmpNum = ''
    for i in range(len(phoneNumber)-1):
        tmpNum += str((int(phoneNumber[i])+int(phoneNumber[i+1])) % 10)
    phoneNumber = tmpNum

print(phoneNumber)