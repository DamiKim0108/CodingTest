import sys
from collections import deque


N, M = map(int, input().split())
computer = [[] for _ in range(N+1)]
result = []


for _ in range(M):
          a, b = map(int, input().split())
          computer[b].append(a)

def bfs(i):
        visited = [0 for _ in range(N+1)]
        q = deque()
        q.append(i)
        visited[i] = 1
        count = 1
        while q:
                i = q.popleft()
                for j in computer[i]:
                        if visited[j] == 0:
                                q.append(j)
                                visited[j] = 1
                                count += 1
        return count

max_count = 1
cnt = 0
for i in range(1, N+1):
          cnt = bfs(i)
          if cnt > max_count:
                  max_count = cnt
                  result = []
                  result.append(i)
          elif cnt == max_count:
                  result.append(i)
print(*result)
          
