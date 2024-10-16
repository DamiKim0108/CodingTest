T = int(input())

for tc in range(1, T+1):
    N = int(input())
    week = list(map(int, input().split()))

    firstDay = []
    answer = 1e9
    
    for i in range(len(week)):
        if week[i] == 1:
            firstDay.append(i)
            
        for day in firstDay:
            idx = day
            total = 0
            rest_days = N
            
            while rest_days:
                if week[idx] == 1:
                    rest_days -= 1
                total += 1
                if idx > 5:
                    idx = 0
                else:
                    idx += 1
                    
            answer = min(answer, total)
    print(f'#{tc} {answer}')