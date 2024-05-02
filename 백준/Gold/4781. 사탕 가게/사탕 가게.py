import sys
input = sys.stdin.readline

while True:
    n, money = map(float,input().rstrip().rsplit())
    n = int(n)

    if n==0 and money==0.00:
        break

    money = int(money * 100)

    candies = []
    for _ in range(n):
        c, p = map(float,input().rstrip().rsplit())
        candies.append([int(c),int(p * 100 + 0.5)])

    dp = [0] * 10001

    for i in range(1,money+1):
        for j in range(n):
            curr_candy_c = candies[j][0]
            curr_candy_m = candies[j][1]

            if (i < curr_candy_m):
                continue

            dp[i] = max(dp[i], dp[i-curr_candy_m] + curr_candy_c)

    print(dp[money])