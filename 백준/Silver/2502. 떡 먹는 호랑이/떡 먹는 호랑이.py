import sys
input = sys.stdin.readline

D, K = map(int, input().split())

dp = [0] * 31

dp[1] = (1, 0)
dp[2] = (0, 1)

for i in range(3, D+1):
          dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

a = dp[D][0]
b = dp[D][1]

n, m = 1, 1
while True:
        tmp = a*n + b*m
        if  tmp == K:
                print(n, m, sep='\n')
                break
        # a와 b 값이 k보다 작다면 b의 값을 하나 키움
        elif tmp < K:
                m += 1
        # a와 b 값이 k보다 크다면 a의 값을 하나 키우고 b는 다시 1부터
        else:
                n += 1
                m = 1