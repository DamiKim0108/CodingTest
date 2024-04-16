import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]

def bfs(x, y):
       queue = deque()
       queue.append((x, y))
       dx = [-1,0,1,0]
       dy = [0,1,0,-1]
       visited[x][y] = 1
       while queue:
              x, y = queue.popleft()
              for d in range(4):
                     nx = x + dx[d]
                     ny = y + dy[d]
                     if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                         queue.append((nx, ny))
                         visited[nx][ny] =  1
                     

visited = [[0]*n for _ in range(n)]
cnt1 = 0

for i in range(n):
          for j in range(n):
              if not visited[i][j]:
                     bfs(i, j)
                     cnt1 += 1

for i in range(n):
       for j in range(n):
              if graph[i][j] == 'G':
                     graph[i][j] = 'R'

visited = [[0]*n for _ in range(n)]
cnt2 = 0

for i in range(n):
       for j in range(n):
              if not visited[i][j]:
                     bfs(i, j)
                     cnt2 += 1

print(cnt1, cnt2)