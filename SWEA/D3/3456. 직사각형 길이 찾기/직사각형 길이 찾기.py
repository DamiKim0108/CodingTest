
T = int(input())
 
for tc in range(1,1+T):
    num_list = list(map(int,input().split()))
    num_list.sort()

    if num_list[0] != num_list[1]:
        print('#{} {}'.format(tc,num_list[0]))
    else:
        print('#{} {}'.format(tc,num_list[2]))