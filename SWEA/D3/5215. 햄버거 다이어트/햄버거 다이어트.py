T = int(input())
def select(data, L):
    N = len(data)
    dp = [[0 for _ in range(L+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, L+1):
            value, cal = data[i-1]
            if cal <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cal] + value)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][L]          
    
for tc in range(1, T+1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = select(data, L)
    print("#{} {}".format(tc, result))

