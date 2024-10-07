def numToXy(num):
    temp = num
    cnt = 0
    xy = [0, 0]

    while True:
        cnt += 1
        temp -= cnt
        if temp <= 0:
            break
    temp = temp + cnt
    xy[0] = temp
    xy[1] = cnt+1-temp
        
    return xy   

def xyToNum(x, y):
        group = (x+y)-1
        start = (((group-1) * group) // 2) + 1
        return start + x - 1

def solve(p, q):
    p_xy = numToXy(p)
    q_xy = numToXy(q)
    x = p_xy[0] + q_xy[0]
    y = p_xy[1] + q_xy[1]
    return xyToNum(x, y)

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())

    result = solve(p, q)
    print('#{} {}'.format(tc, result))
