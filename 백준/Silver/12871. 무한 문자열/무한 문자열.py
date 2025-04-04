def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

s = input()
t = input()

len_s = len(s)
len_t = len(t)

lcm_st = lcm(len_s, len_t)

s *= lcm_st // len_s
t *= lcm_st // len_t

if s == t:
    print(1)
else:
    print(0)