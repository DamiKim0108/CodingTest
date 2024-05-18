T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    # dp 사용 (for문 i, 0~i / lst[i]>lst[j] 면 dp[i], dp[j]+1 중 max)
    dp = [1] * N
    
    for i in range(1, N):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j]+1)
                
    print(f'#{tc} {max(dp)}')