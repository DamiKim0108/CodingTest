def dfs(cnt):
    global answer
    
    if cnt == count:
        temp = int(''.join(num))
        answer = max(answer, temp)
        return
    
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            num[i], num[j] = num[j], num[i]
            temp = int(''.join(num))
            
            if (temp, cnt) not in visited:
                visited[(temp, cnt)] = 0
                dfs(cnt+1)
                # 끝까지 돌았다면 다시 원상복구 
            num[i], num[j] = num[j], num[i]
                

T = int(input())

for tc in range(1, T+1):
    num, count = map(int, input().split())
    num = list(str(num))
    answer = 0
    
    visited = {}
    dfs(0)
    print("#{} {}".format(tc, answer))