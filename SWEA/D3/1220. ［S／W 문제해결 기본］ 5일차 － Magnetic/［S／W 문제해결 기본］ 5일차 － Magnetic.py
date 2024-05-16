T = 10

for tc in range(1, T+1):
    n = int(input())

    table = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    
    for j in range(n):
        state = 0
        for i in range(n):
            if table[i][j] == 1:
                state = 1
            if table[i][j] == 2 and state == 1:
                ans += 1
                state = 0
    print(f'#{tc} {ans}')


