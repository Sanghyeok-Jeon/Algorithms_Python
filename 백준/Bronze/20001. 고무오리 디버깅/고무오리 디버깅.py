problem = 0
while True:
    data = input()
    
    if data == '고무오리 디버깅 끝':
        break
    
    if data == '문제':
        problem += 1
    elif data == '고무오리':
        if not problem:
            problem += 2
        else:
            problem -= 1
            
if problem:
    print('힝구')
else:
    print('고무오리야 사랑해')