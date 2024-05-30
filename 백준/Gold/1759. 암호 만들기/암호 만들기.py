# 암호 조건을 만족하는지 확인하는 함수
def check_password(password):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_cnt = 0
    consonant_cnt = 0
    
    # 암호에 포함된 자음과 모음의 개수를 세기
    for c in password:
        if c in vowels:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
    
    # 조건에 맞는 암호인지 확인
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        return True
    else:
        return False

# 암호 조건을 만족하는지 확인하는 함수 
def generate_password(pw, cnt, idx):
    # 암호의 길이가 L에 도달하면 조건을 만족하는지 확인하고 출력
    if cnt == L:
        if check_password(pw):
            print(pw)
        return
    
    # 알파벳 조합 생성
    for i in range(idx, C):
        generate_password(pw+data[i], cnt+1, i+1)
    
L, C = map(int, input().split())
data = sorted((input().split()))

generate_password('', 0, 0)