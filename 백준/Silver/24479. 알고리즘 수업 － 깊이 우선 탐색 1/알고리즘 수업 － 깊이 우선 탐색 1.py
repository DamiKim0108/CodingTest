import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
c = 1

def dfs(graph, x, visited):
        global c
        visited[x] = c
        for i in graph[x]:
                if visited[i] == 0:
                        c += 1
                        dfs(graph, i, visited)



for _ in range(m):
          u, v = map(int, input().split())
          graph[u].append(v)
          graph[v].append(u)

for i in range(n+1):
        graph[i].sort()

dfs(graph, r, visited)

for i in range(1, n+1):
        print(visited[i])