import sys

def divide(length, start_r, start_c):
    global cnt

    if start_r == r and start_c == c:
        print(cnt)
        return

    if length == 1:
        cnt += 1
        return

    if not (start_r <= r < start_r + length and start_c <= c < start_c + length):
        cnt += length ** 2
        return

    divide(length//2, start_r, start_c)
    divide(length//2, start_r, start_c + length//2)
    divide(length//2, start_r + length//2, start_c)
    divide(length//2, start_r + length//2, start_c + length//2)

N, r, c = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

divide(2**N, 0, 0)