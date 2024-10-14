T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    items = [list(map(int, input().split()))for _ in range(N)]


    result = []

    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, len(dp)):
        v, c = items[i-1]
        for j in range(1, len(dp[i])):
            if j >= v:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-v]+c)
            else:
                dp[i][j] = dp[i-1][j]
                
    result.append(dp[-1][-1])
    print('#{} {}'.format(tc, result[-1]))