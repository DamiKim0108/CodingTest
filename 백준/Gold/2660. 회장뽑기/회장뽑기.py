import sys
from collections import deque
unput = sys.stdin.readline

N = int(input())
friend = [[] for _ in range(N+1)]

while True:
          a, b = map(int, input().split())

          if a == -1:
                  break
          else:
                  friend[a].append(b)
                  friend[b].append(a)

def bfs(n):
        visited[n] = True
        q = deque()
        q.append(n)

        while q:
                x = q.popleft()
                for i in friend[x]:
                        if not visited[i]:
                                q.append(i)
                                dist[i] = dist[x] + 1
                                visited[i] = True

chairman = []
d = 51

for i in range(1, N+1):
        dist = [0] * (N+1)
        visited = [False] * (N+1)
        bfs(i)

        m = max(dist)

        if m == d:
                chairman.append(i)
        elif m < d:
                chairman = [i]
                d = m
          
print(d, len(chairman))
print(*chairman)
