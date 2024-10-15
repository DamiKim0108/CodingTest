T = int(input())

for tc in range(1, T+1):
    win = 0
    game = list(input())

    for item in game:
        if item == 'o':
            win += 1
            
    if (15-len(game)) + win >= 8:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')