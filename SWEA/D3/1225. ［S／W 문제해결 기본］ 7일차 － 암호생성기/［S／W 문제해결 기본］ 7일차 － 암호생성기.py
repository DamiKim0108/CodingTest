def password(list):
    while True:
        for i in range(1, 6):  
            num = list.pop(0)
            list.append(num - i) 

            if list[-1] <= 0: 
                list[-1] = 0   
                return list

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    numbers = list(map(int, input().split()))
    result = password(numbers)

    print('#{}'.format(tc), *result)
