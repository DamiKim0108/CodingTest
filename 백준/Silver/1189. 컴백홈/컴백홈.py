R, C, K = map(int, input().split())

visited = [[0]*C for _ in range(R)]
map = []

for _ in range(R):
          map.append(list(input().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def DFS(x, y, distance):
        global answer

        if distance == K and y == C-1 and x == 0:
                answer += 1

        else:
                map[x][y] = 'T'

                for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if (0 <= nx < R and 0 <= ny < C and map[nx][ny] == '.'):
                                map[nx][ny] = 'T'
                                DFS(nx, ny, distance+1)

                                map[nx][ny] = '.'

DFS(R-1, 0, 1)
print(answer)

