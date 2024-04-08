n = list(map(int, input().rstrip()))
dp = [[0 for _ in range(35)] for _ in range(len(n))]
dp[0][n[0]] = 1

for i in range(1, len(n)):
          for j in range(1, 35):
                  next = 10*j + n[i]

                  if next <= 34:
                          dp[i][next] += dp[i-1][j]
                  dp[i][n[i]] += dp[i-1][j]

print(sum(dp[-1][1:]))
