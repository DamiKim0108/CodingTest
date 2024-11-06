T = int(input())
for case in range(1,T+1):
    lst = [list(input()) for _ in range(5)]
    result = [[0]*15 for _ in range(15)] 
    print(f'#{case} ',end = '')

    for i in range(5):
        for j in range(len(lst[i])):
            result[j][i] = lst[i][j] 

    for i in range(15):
        for j in range(15):
            if result[i][j] != 0: #0이 아닌부분 출력
                print(result[i][j], end='')
    print()
