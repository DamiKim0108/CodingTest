T = int(input())

for tc in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())
    result = 0

    cost_a = P * W
    if W <= R:
    	cost_b = Q
    elif W > R:
    	cost_b = Q + ((W-R)*S)

    result = min(cost_a, cost_b)

    print(f"#{tc} {result}")