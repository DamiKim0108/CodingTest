T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time.sort()

    result = "Possible"

    for i in range(N):
        boong = (arrive_time[i] // M) * K - (i+1)
        if boong < 0:
            result = "Impossible"
            break

    print("#{} {}".format(tc, result))