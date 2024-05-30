def lcs(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # LCS 길이 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:    # 현재 문자가 같은 경우
                dp[i][j] = dp[i - 1][j - 1] + 1    # 대각선 위츼 값 + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])    # 왼쪽 값 또는 위쪽값 중 최댓값 선택

    # LCS 문자열 찾기
    lcs_length = dp[n][m]
    lcs_str = ''
    i = n
    j = m
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:    # 현재 문자가 같은 경우
            lcs_str = str1[i - 1] + lcs_str    # 현재 문자를 LCS 문자열에 추가
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:    # 왼쪽 값이 더 큰 경우
            i -= 1    # 위쪽으로 이동
        else:    # 위쪽 값이 더 큰 경우
            j -= 1    # 왼쪽으로 이동

    return lcs_length, lcs_str

str1 = input()
str2 = input()

lcs_length, lcs_str = lcs(str1, str2)

print(lcs_length)
print(lcs_str)