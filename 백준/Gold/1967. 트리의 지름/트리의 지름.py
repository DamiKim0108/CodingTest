import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, now):
        for a, b in tree[start]:
                if visited[a] == -1:
                        visited[a] = b + now
                        dfs(a, visited[a])

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
          a, b, c = map(int, input().split())
          tree[a].append([b, c])
          tree[b].append([a, c])

visited = [-1]*(n+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1]*(n+1)
visited[start] = 0
dfs(start, 0)
print(max(visited))