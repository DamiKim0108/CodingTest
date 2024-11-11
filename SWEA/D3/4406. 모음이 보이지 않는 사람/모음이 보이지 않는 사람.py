T = int(input())

for tc in range(1, T + 1):
    data = input()
    result = []

    for i in range(len(data)):
        if data[i] in ['a', 'e', 'i', 'o', 'u']:
            continue
        result.append(data[i])

    print('#{} {}'.format(tc, ''.join(result)))
