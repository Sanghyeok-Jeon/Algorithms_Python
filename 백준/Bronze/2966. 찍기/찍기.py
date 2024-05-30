N = int(input())
correct = input()
checkA = 'ABC'
checkB = 'BABC'
checkG = 'CCAABB'

correctABG = [0, 0, 0]
for i in range(N):
    if checkA[i % 3] == correct[i]:
        correctABG[0] += 1
    
    if checkB[i % 4] == correct[i]:
        correctABG[1] += 1
        
    if checkG[i % 6] == correct[i]:
        correctABG[2] += 1
        
maxCorrect = max(correctABG)
print(maxCorrect) 
if correctABG[0] == maxCorrect:
    print('Adrian')
if correctABG[1] == maxCorrect:
    print('Bruno')
if correctABG[2] == maxCorrect:
    print('Goran')