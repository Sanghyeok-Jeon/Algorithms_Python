w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

if ((p + t) // w) % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if ((q + t) // h) % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)