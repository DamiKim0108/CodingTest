def sudoku(arr):
    for i in range(9):
        lst_h = [0] * 10
        lst_v = [0]*10
        for j in range(9):
            lst_h[arr[i][j]] += 1
            if lst_h[arr[i][j]] == 2:
                return 0
            lst_v[arr[j][i]] += 1
            if lst_v[arr[j][i]] == 2:
                return 0
            
    for x in range(0,9,3):
        for y in range(0,9,3):
            lst_3 = [0] * 10
            for i in range(3):
                for j in range(3):
                    lst_3[arr[x+i][y+j]] += 1
                    if lst_3[arr[x+i][y+j]] == 2:
                        return 0
    return 1

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    result = sudoku(arr)
    print(f'#{tc} {result}')