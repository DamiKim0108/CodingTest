T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    idx, cnt = 0, 0

    for j in range(N):
        while True:
            if idx == M or A[j] <= B[idx]:
                cnt += idx
                break
            else:
                idx += 1
    print(cnt)