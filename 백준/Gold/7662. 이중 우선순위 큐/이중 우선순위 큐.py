import sys
import heapq
T = int(input())
for _ in range(T):
    k = int(input())
    maxhq = []
    minhq = []
    visited = [0]*k  

    for i in range(k):
        command, num = sys.stdin.readline().split()
     
        if command == 'I':
            heapq.heappush(maxhq,((-1)*int(num),i))
            heapq.heappush(minhq,(int(num),i))
        
        elif command == 'D':
            if num == '-1': 
                while minhq:
                    if visited[minhq[0][1]] == 1:
                        heapq.heappop(minhq)
                    else:
                        break
                if minhq:
                    min = minhq[0][1]
                    visited[min] = 1
                    heapq.heappop(minhq)
                    
            elif num == '1':
                while maxhq:
                    if visited[maxhq[0][1]] == 1:
                        heapq.heappop(maxhq)
                    else:
                        break
                if maxhq:
                    max = maxhq[0][1]
                    visited[max] = 1
                    heapq.heappop(maxhq)
            
    while maxhq:
            if visited[maxhq[0][1]] == 1:
                heapq.heappop(maxhq)
            else:
                break
    while minhq:
            if visited[minhq[0][1]] == 1:
                heapq.heappop(minhq)
            else:
                break
    if minhq:
        print((-1)*maxhq[0][0], minhq[0][0])
    else:
        print("EMPTY")