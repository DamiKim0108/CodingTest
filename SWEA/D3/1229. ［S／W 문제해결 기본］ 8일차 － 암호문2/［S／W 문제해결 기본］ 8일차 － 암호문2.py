for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    Q = int(input())
    order = list(input().split())

    for i in range(len(order)):
        if order[i] == 'I':
            I_num = order[i+3:i+3+int(order[i+2])]
            a = 0
            for j in range(len(I_num)):
                password.insert(int(order[i+1])+a, I_num[j])
                a += 1
                
        elif order[i] == 'D':
            for idx in range(int(order[i+2])):
                password.pop(int(order[i+1]))
                
    print(f'#{tc}', end =' ')
    for i in range(10):
        print(password[i], end=' ')
    print()


                  
