import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

max = 100001

def bfs():
          
          time = [-1]*max
          time[n] = 0
          q = deque([n])

          while q:
                  x = q.popleft()
                  if x == k:
                          return time[x]
                  
                  for nx in (x-1, x+1, x*2):
                          # 이동하는 곳이 범위 내에 있고 방문하지 않았다면 이동
                          if 0<= nx <= 100000 and time[nx] == -1:
                                  if nx == 2*x:
                                          time[nx] = time[x]
                                          q.appendleft(nx)
                                  else:
                                          time[nx] = time[x] + 1
                                          q.append(nx)
print(bfs())
          