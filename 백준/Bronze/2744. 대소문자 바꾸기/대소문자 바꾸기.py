data = input()
result = ''
for d in data:
    if d.islower():
        result += d.upper()
    else:
        result += d.lower()

print(result)