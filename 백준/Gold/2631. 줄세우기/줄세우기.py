import sys
input = sys.stdin.readline

n = int(input())

dp = [1] * (n+1)
num = [0]
num = [int(input()) for _ in range(n)]

for i in range(1, n):
          for j in range(0, i):
                  if num[j] < num[i]:
                          dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))