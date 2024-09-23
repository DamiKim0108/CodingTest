for _ in range(10):
    tc = int(input())
    result, cross, cross1 = 0, 0, 0
    column = [0 for _ in range(100)]
   

    for i in range(100):
        # 가로 합 저장
        row = list(map(int, input().split()))
        result = max(result, sum(row))

        # 오른쪽 대각선
        cross += row[i]
        # 왼쪽 대각선
        cross1 += row[99-i]

        for j in range(100):
            column[j] += row[j]
             
    result = max(result, max(column), cross, cross1)
    print(f'#{tc} {result}') 