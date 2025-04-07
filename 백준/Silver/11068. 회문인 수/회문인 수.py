def is_palindrome(s):
    return s == s[::-1]

def convert_to_base(n, base):
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits

def is_palindrome_in_any_base(n):
    for base in range(2, 65):
        if is_palindrome(convert_to_base(n, base)):
            return True
    return False

def main():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        if is_palindrome_in_any_base(n):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()