TC = 10

for tc in range(TC):
    result = 0
    N = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(2, N-2):
        arrMax = max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
        if arr[i] > arrMax:
            result += (arr[i]-arrMax)
            
    print("#{} {}".format(tc+1, result))