T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()

    cnt = 0
    result = 'Possible'

    for i in range(N):
        cnt = (customer[i] // M) * K - (i+1)
        if cnt < 0:
            result = 'Impossible'
            break
            
    print('#{} {}'.format(tc, result))
                  
