T = int(input())

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 1, -1, 0, 1, -1, 0]

def dfs(i, j, d, count):
        global result

        if count >= 5:
                result = 'YES'
                return
        nx = i + dx[d]
        ny = j + dy[d]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                return
        if graph[nx][ny] == 1:
                count += 1
                dfs(nx, ny, d, count)
        else:
                return
               
for tc in range(1, T+1):
    N = int(input())
    result = 'NO'
    graph = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        line = input().rstrip()
        for j, val in enumerate(line):
            if val == '.':
                graph[i][j] = 0
            else:
                graph[i][j] = 1
                
    for i in range(N):
        for j in range(N):
            if graph[i][j]==1:
                for d in range(8):
                    dfs(i,j,d,1)
            if result=="YES":
                break
    print('#{} {}'.format(tc, result))
