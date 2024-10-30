T = int(input())

for tc in range(1, T+1):
    N = int(input())

    cards = list(input().split())
    idx = 0
    idx2 = 0
    result = []
    temp = 0

    if N%2==0:
        idx = N//2
        idx2 = N//2
    if N%2!=0:
        idx = N//2 + 1
        idx2 = N//2 + 1
        
    while idx2 < N:
        result.append(cards[temp])
        result.append(cards[idx2])
        temp += 1
        idx2 += 1
        if N%2!=0 and temp == idx-1:
            result.append(cards[temp])
    print(f'#{tc} {" ".join(result)}')
