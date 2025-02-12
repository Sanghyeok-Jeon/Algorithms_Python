def min_flips(s):
    # 첫 번째 문자의 그룹을 카운트
    count_0 = 0 if s[0] == '1' else 1
    count_1 = 0 if s[0] == '0' else 1

    # 문자열을 순회하며 그룹의 변화를 체크
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            if s[i] == '1':
                count_1 += 1
            else:
                count_0 += 1

    # 두 그룹 중 더 작은 값을 선택
    return min(count_0, count_1)

# 입력 처리
S = input().strip()

# 결과 출력
print(min_flips(S))