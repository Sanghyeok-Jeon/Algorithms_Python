import sys

def main():
    target = sys.stdin.readline().strip()
    
    idx = 0
    num = 1

    while idx < len(target):
        for ch in str(num):
            if idx < len(target) and target[idx] == ch:
                idx += 1
        num += 1

    print(num - 1)

if __name__ == "__main__":
    main()