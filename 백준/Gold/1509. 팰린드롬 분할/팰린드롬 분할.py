def is_palindrome(s):
    # 문자열 s가 팰린드롬인지 확인하는 함수
    return s == s[::-1]

def palindrome_partition(s):
    n = len(s)
    dp = [0]* n  # dp[i]는 문자열 s의 0부터 i까지의 최소 분할 수

    for end in range(n):
        min_cut = end  # 최소 분할 수는 최대로 설정
        for start in range(end+1):
            if is_palindrome(s[start:end+1]):
                if start == 0:
                    min_cut = 0  # start가 0인 경우는 분할이 필요하지 않음
                else:
                    min_cut = min(min_cut, dp[start-1]+ 1)  # start부터 end까지의 최소 분할 수 갱신
        dp[end]= min_cut

    return dp[n-1] # 문자열 전체의 최소 분할 수 반환

# 입력 받기
s = input()

# 결과 출력
print(palindrome_partition(s) + 1)