T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    report = list(map(int, input().split()))

    student = []
    for i in range(1, N+1):
        student.append(i)
    
    for num in range(len(report)):
        student.pop(student.index(report[num]))
        
    print(f'#{tc}', *student)

