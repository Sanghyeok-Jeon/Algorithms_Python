import sys

input = sys.stdin.readline
s, n = input().split()
s = int(s)
digits = list(n)

# 7-seg segments: a(top), b(upper-right), c(lower-right), d(bottom),
# e(lower-left), f(upper-left), g(middle)
seg = {
    '0': set("ab cdef".replace(" ", "")),  # a b c d e f
    '1': set("bc"),
    '2': set("abged"),
    '3': set("abgcd"),
    '4': set("fgbc"),
    '5': set("afgcd"),
    '6': set("afgcde"),
    '7': set("abc"),
    '8': set("abcdefg"),
    '9': set("abfgcd"),
}

height = 2 * s + 3
width = s + 2

def render_digit(d: str, row: int) -> str:
    on = seg[d]

    # Top horizontal (row 0): segment a
    if row == 0:
        mid = '-' * s if 'a' in on else ' ' * s
        return ' ' + mid + ' '

    # Upper verticals (rows 1..s): segments f (left), b (right)
    if 1 <= row <= s:
        left = '|' if 'f' in on else ' '
        right = '|' if 'b' in on else ' '
        return left + (' ' * s) + right

    # Middle horizontal (row s+1): segment g
    if row == s + 1:
        mid = '-' * s if 'g' in on else ' ' * s
        return ' ' + mid + ' '

    # Lower verticals (rows s+2..2s+1): segments e (left), c (right)
    if s + 2 <= row <= 2 * s + 1:
        left = '|' if 'e' in on else ' '
        right = '|' if 'c' in on else ' '
        return left + (' ' * s) + right

    # Bottom horizontal (row 2s+2): segment d
    mid = '-' * s if 'd' in on else ' ' * s
    return ' ' + mid + ' '

out_lines = []
for r in range(height):
    parts = [render_digit(d, r) for d in digits]
    out_lines.append(' '.join(parts))

sys.stdout.write('\n'.join(out_lines))