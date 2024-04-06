C, N = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
# 적어도 C명을 늘린다고 했음으로 C + 100
dp = [INF for _ in range(C+100)]
dp[0] = 0

for c, n in info:
          for i in range(n, C + 100):
                  dp[i] = min(dp[i], dp[i-n] + c)

print(min(dp[C:]))