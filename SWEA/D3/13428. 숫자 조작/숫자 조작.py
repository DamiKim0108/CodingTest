T = int(input())

for tc in range(1, T+1):
    N = list(input())
    max_num, min_num = ''.join(N), ''.join(N)

    for i in range(len(N)-1):
        for j in range(i+1, len(N)):
            if i==0 and N[j] == '0':
                continue
                
            N[i], N[j] = N[j], N[i]
            
            min_num = min(min_num, ''.join(N))
            max_num = max(max_num, ''.join(N))
            
            N[i], N[j] = N[j], N[i]
            
    print('#{} {} {}'.format(tc, min_num, max_num))


