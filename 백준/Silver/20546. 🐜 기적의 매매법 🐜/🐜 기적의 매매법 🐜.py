import sys
input = sys.stdin.readline
def solution():
    money = int(input())  # 시드머니
    prices = list(map(int, input().split()))  # 주가 리스트

    # 준현이의 자산 계산 (BNP 전략)
    stock_bnp = 0
    money_bnp = money
    for price in prices:
        if money_bnp >= price:
            stock_bnp += money_bnp // price  # 살 수 있는 만큼 매수
            money_bnp %= price  # 남은 돈
    bnp_total = money_bnp + stock_bnp * prices[-1]  # 마지막 날의 주가로 자산 계산

    # 성민이의 자산 계산 (TIMING 전략)
    stock_timing = 0
    money_timing = money
    up_count = 0
    down_count = 0
    for i in range(4, len(prices)):
        tmp = prices[i - 3:i + 1]

        if tmp[0] > tmp[1] > tmp[2] and money_timing >= tmp[3]:
            stock_timing += money_timing // tmp[3]
            money_timing %= tmp[3]
        elif tmp[0] < tmp[1] < tmp[2] and stock_timing > 0:
            money_timing += stock_timing * tmp[3]
            stock_timing = 0

    timing_total = money_timing + stock_timing * prices[-1]  # 마지막 날의 주가로 자산 계산

    # 결과 비교 및 출력
    if bnp_total > timing_total:
        print("BNP")
    elif bnp_total < timing_total:
        print("TIMING")
    else:
        print("SAMESAME")

solution()