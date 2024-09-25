for tc in range(1, 11):
    N = int(input())
    find = input()
    texts = input()

    cnt = 0
    for i in range(0, len(texts)-1):
        if texts[i] == find[0]:
            if texts[i:i+len(find)] == find:
                cnt += 1
    print('#{} {}'.format(tc, cnt))