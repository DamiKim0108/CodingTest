import sys
input = sys.stdin.readline

T = int(input())

while T:
          N = int(input())
          coin = list(map(int, input().split()))
          M = int(input())
          d = [0 for _ in range(M+1)]
          d[0] = 1

          for i in range(N):
                  for j in range(coin[i], M+1):
                          d[j] += d[j-coin[i]]

          print(d[M])
          T -= 1
                                    