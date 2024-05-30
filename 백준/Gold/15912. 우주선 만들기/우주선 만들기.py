def min_cost(N, W, E):
    prices = [0] * (N + 1)

    for i in range(1, N+1):
        max_w = W[i]
        max_e = E[i]

        # 직전까지의 부품값 + 현재 부품값
        prices[i] = prices[i-1] + max_w * max_e

        # 역순으로 가면서 j~i 사이의 부품값 계산
        for j in range(i-1, 0, -1):
            prev_w = W[j]
            prev_e = E[j]

            max_w = max(prev_w, max_w)
            max_e = max(prev_e, max_e)

            interval_price = max_w * max_e

            # j~i 사이의 부품값 + j-1의 부품값
            prices[i] = min(prices[i], prices[j-1] + interval_price)

    return prices[-1]

N = int(input())
W = [0] + list(map(int, input().split()))
E = [0] + list(map(int, input().split()))

result = min_cost(N, W, E)

print(result)