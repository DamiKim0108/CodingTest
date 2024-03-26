import sys

input = sys.stdin.readline

R, C = map(int, input().split())
map = []

for _ in range(R):
          map.append(list(input()))

answer = 0
alpha = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y, count):
        global answer
        answer = max(answer, count)

        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <=  ny < C and not map[nx][ny] in alpha:
                        alpha.add(map[nx][ny])
                        DFS(nx, ny, count + 1)
                        alpha.remove(map[nx][ny])       

alpha.add(map[0][0])
DFS(0, 0, 1)

print(answer)