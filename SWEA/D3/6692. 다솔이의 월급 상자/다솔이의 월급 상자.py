T = int(input())

for tc in range(1, T+1):
    N = int(input())

    avg = 0
    for i in range(N):
        p, x = input().split()
        avg += float(p) * int(x)

    print(f'#{tc} {avg:.6f}')