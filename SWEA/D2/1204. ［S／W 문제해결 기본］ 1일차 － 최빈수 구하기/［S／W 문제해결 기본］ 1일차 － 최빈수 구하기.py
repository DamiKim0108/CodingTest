T = int(input())
for i in range(T):
    num = int(input())
    li = list(map(int, input().split()))
    dic = {}

    for i in li:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0

    print("#"+str(num), max(dic, key=dic.get))
