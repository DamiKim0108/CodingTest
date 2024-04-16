import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [[x for x in array] for _ in range(2)]

for i in range(1, n):
          dp[0][i] = max(dp[0][i-1]+array[i], dp[0][i])
          dp[1][i] = max(dp[1][i-1]+array[i], dp[0][i-1])

print(max(max(dp[0]), max(dp[1])))
      