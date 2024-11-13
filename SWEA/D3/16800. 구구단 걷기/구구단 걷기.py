T = int(input())

for tc in range(1, T+1):
    N = int(input())

    res = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans = (i-1) + (N//i-1)
            res.append(ans)

    print(f'#{tc} {res[-1]}')