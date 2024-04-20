import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

x, y, z = len(a), len(b), len(c)

graph = [[[0] * (z+1) for _ in range(y+1)] for _ in range(x+1)]

for i in range(1, x+1):
          for j in range(1, y+1):
                  for k in range(1, z+1):
                          if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                                  graph[i][j][k] = graph[i-1][j-1][k-1] + 1
                          else:
                                  graph[i][j][k] = max(graph[i][j][k-1], graph[i][j-1][k], graph[i-1][j][k])

print(graph[x][y][k])