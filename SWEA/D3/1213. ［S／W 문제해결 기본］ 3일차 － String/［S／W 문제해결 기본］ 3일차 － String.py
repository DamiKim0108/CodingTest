T = 10

for tc in range(1, T+1):
    Tc = int(input())
    search = input()
    string = input()
    
    ans = string.count(search)
    
    print(f'#{tc} {ans}')