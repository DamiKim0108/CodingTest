T = int(input())

for tc in range(1, T+1):
    N = input() 
    num_list = sorted(list(N)) 
    k = 2
    flag = False
    
    while True:
        new = int(N) * k 
        if len(str(new)) > len(N): 
            break
        if sorted(list(str(new))) == num_list:
            flag = True
            break
        k += 1

    if flag:
        answer = "possible"
    else:
        answer = "impossible"

    print(f"#{tc} {answer}")