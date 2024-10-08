T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    binary = []
    # 이진수 변환
    # bin 함수로 이진수로 변환
    # 앞에 표현된 '0b'를 제거해야 함
    M = list(map(int, bin(M)[2:]))
    M.reverse()

    result = 'ON'

    if M[:N].count(1) == N:
        print('#{} {}'.format(tc, result))
    else:
        result = 'OFF'
        print('#{} {}'.format(tc, result))



          
                  

