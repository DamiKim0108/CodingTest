import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]

for _ in range(K):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def dfs(x, y):
        global count
        for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0<= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        count += 1
                        dfs(nx, ny)
                    
res = 0

for i in range(N):
        for j in range(M):
                if graph[i][j] == 1:
                        count = 0
                        dfs(i, j)
                        res = max(res, count)
print(res)
