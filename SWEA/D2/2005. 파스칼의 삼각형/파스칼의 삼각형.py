T = int(input())

for tc in range(1, T+1):
    N = int(input())

    graph = [[0] * N for _ in range(N)]
    graph[0][0] = 1

    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                graph[i][j] = 1
            else:
                graph[i][j] = graph[i-1][j-1] + graph[i-1][j]
                
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                print(graph[i][j], end=' ')
        print()