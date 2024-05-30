num = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,
       'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

result = 0
result += num[input()] * 10
result += num[input()]
result *= 10**num[input()]
print(result)