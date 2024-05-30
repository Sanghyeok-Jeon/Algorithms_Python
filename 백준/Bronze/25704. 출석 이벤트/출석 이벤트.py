N = int(input())
P = int(input())

result = 0
if N >= 20:
    result = min(P * 0.75, P - 2000)
elif N >= 15:
    result = min(P - 2000, P * 0.9)
elif N >= 10:
    result = min(P * 0.9, P - 500)
elif N >= 5:
    result = P - 500
else:
    result = P

print(int(result) if int(result) > 0 else 0)