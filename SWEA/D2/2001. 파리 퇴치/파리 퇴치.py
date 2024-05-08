t = int(input())

for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    result = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_val = 0
            for k in range(m):
                for l in range(m):
                    sum_val += board[i+k][j+l]
            if sum_val > result:
                result = sum_val
                
    print(f'#{tc} {result}')