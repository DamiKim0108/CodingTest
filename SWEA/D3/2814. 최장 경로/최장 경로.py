def dfs(v, count):
    global max_len
    
    # v 노드 방문처리, v 노드와 연결된 점들 중 방문 안한 노드 방문
    visited[v] = 1
    
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, count+1)
            
    # 방문할 수 있는 점이 없다면 방문처리 취소 -> 다른 경로에서 지나갈 수 있음        
    visited[v] = 0
    
    if count > max_len:
        max_len = count


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    count, max_len = 0, 0
    
    for i in range(1, N+1):
        dfs(i, 1)
        
    print(f'#{tc} {max_len}')