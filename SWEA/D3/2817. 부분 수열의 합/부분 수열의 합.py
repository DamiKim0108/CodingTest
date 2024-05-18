def dfs(index, sum = 0):
    global count

    if sum == K:
        count +=1
        return 

    if index == N:
        return

    dfs(index+1, sum + data[index])
    dfs(index+1, sum) 

tc = int(input())
for i in range(tc):
    N, K = map(int, input().split())
    count = 0
    data = list(map(int,input().split()))
    dfs(0)
    print('#{} {}'.format(i+1, count))