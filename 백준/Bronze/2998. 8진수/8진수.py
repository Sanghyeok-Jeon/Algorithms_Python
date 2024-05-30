originNum = input()
target = '0' * (3-len(originNum)%3) + originNum if len(originNum)%3 else originNum
octalTable = {'000' : '0', '001' : '1', '010' : '2', '011' : '3', '100' : '4', '101' : '5', '110' : '6', '111' : '7'}

answer = ''
for i in range(0, len(target), 3):
    answer += octalTable[target[i:i+3]]
    
print(answer)