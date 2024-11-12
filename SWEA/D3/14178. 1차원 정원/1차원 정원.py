T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())

    flag = 2*D + 1
    result = 0
    result = N // flag

    if N % flag != 0:
        result += 1

    print('#{} {}'.format(tc, result))

