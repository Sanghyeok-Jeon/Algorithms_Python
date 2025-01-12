N = int(input())
for _ in range(N):
    result_coin = input()

    three_coin_seq = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    for i in range(38):
        three_coin_seq[result_coin[i:i + 3]] += 1

    print(*three_coin_seq.values())
