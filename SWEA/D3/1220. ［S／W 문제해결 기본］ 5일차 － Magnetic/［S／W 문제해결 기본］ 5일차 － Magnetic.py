

for tc in range(1, 11):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for j in range(N):
        flag = 0
        for i in range(N):
            if graph[i][j] == 1:
                flag = 1
            if graph[i][j] == 2 and flag == 1:
                count += 1
                flag = 0
    print(f'#{tc} {count}')
