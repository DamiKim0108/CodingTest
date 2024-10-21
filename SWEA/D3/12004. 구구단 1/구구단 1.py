T = int(input())

for tc in range(1, T+1):
    N = int(input())

    flag = False
    idx = 1
    answer = 'No'
    temp = 0

    while True:
        if idx > 9:
            break
        temp = N // idx

        if N % idx == 0:
            if temp < 10 and temp > 0:
                flag = True
                break
            else:
                idx += 1
        else:
            idx += 1
            
    if flag:
        answer = 'Yes'
        print(f'#{tc} {answer}')
    else:
        print(f'#{tc} {answer}')