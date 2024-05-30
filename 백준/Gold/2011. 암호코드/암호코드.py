def count_decodings(code):
    n = len(code)
    dp = [0] * (n + 1)
    dp[0] = 1    # 빈 문자열은 1가지 경우의 수

    # 한 자리 수 암호 해석 가능한 경우
    if code[0] != '0':
        dp[1] = 1

    for i in range(2, n+1):
        # 한 자리 수로 해석 가능한 경우
        if code[i-1] != '0':
            dp[i] += dp[i-1]

        # 두 자리 수로 해석 가능한 경우
        two_digit = int(code[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]

    return dp[n] % 1000000

code = input()

result = count_decodings(code)

print(result)