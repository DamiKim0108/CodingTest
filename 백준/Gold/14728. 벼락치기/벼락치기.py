import sys
input = sys.stdin.readline

N, T = map(int, input().split())

time, score = [0], [0]

for _ in range(N):
          t, s = map(int, input().split())
          time.append(t)
          score.append(s)

dp = [[0]*(T+1) for _ in range(N+1)]

# i개의 단원 중 j시간 공부했을 때 얻을 수 있는 최대 점수
# j가 현재 과목인 i를 공부할 때 드는 시간보다 크거나 같으면
# 현재 과목 i를 공부 할 시간이 있는 것임으로
# 현재 과목 공부를 안했을 때와 현재 과목을 공부했을때의 시간을 비교한다
# 현재 과목을 공부하지 않았을 때의 최대 점수와 현재 과목을 공부하기 전의 점수 + 현재 과목의 점수 비교

for i in range(1, N+1):
        for j in range(1, T+1):
                if j>=time[i]:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]]+score[i])
                else:
                        dp[i][j] = dp[i-1][j]
print(dp[N][T])