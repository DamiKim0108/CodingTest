T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(Ｎ)]

    mid = N//2
    result = 0

    for i in range(N):
        if i <= mid:
            result += sum(farm[i][mid-i:mid+i+1])
        else:
            result += sum(farm[i][i-mid:N-(i-mid)])
    print("#{} {}".format(tc, result))
