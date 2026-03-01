import sys

def is_palindrome(t: str) -> bool:
    return t == t[::-1]

def main():
    s = sys.stdin.readline().strip()
    n = len(s)

    for i in range(n):
        if is_palindrome(s[i:]):
            print(n + i)
            return

if __name__ == "__main__":
    main()