for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    t1 = 3600*h1 + 60*m1 + s1
    t2 = 3600*h2 + 60*m2 + s2
    t = t2 - t1

    h = t//3600
    m = (t-h*3600)//60
    s = t%60
    
    print(h, m, s)