import sys
from collections import deque
input = sys.stdin.readline
board = [0] * 101
visited = [False] * 101

N, M = map(int, input().split())
ladder = dict()
snake = dict()

for _ in range(N):
          a, b = map(int, input().split())
          ladder[a] = b

for _ in range(M):
        a, b = map(int, input().split())
        snake[a] = b
q = deque([1])
while q:
        x = q.popleft()

        if x == 100:
                print(board[x])
                break
        for dice in range(1, 7):
                next = x + dice

                if next <= 100 and not visited[next]:
                        if next in ladder.keys():
                                next = ladder[next]
                        if next in snake.keys():
                                next = snake[next]
                        if not visited[next]:
                                visited[next] = True
                                board[next] = board[x] + 1
                                q.append(next)