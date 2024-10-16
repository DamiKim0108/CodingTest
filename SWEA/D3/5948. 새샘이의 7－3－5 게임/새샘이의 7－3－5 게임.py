T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int, input().split()))


    ans = set()
    score = 0

    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            for k in range(j+1, len(num_list)):
                score = num_list[i] + num_list[j] + num_list[k]
                ans.add(score)
                
    res = list(ans)
    res.sort()
    
    print(f'#{tc} {res[-5]}')



          