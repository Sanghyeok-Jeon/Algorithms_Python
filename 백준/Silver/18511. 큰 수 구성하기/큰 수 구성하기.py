def find_largest_number(N, digits):
    str_N = str(N)
    length = len(str_N)

    largest_number = 0

    def dfs(current):
        nonlocal largest_number
        if int(current) > N:
            return

        largest_number = max(largest_number, int(current))
        
        if len(current) < length:
            for digit in digits:
                dfs(current + digit)

    for digit in digits:
        dfs(digit)

    return largest_number

N, K = map(int, input().split())
digits = input().split()

print(find_largest_number(N, digits))
