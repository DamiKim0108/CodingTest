T = int(input())

def chk(num):
    num_str = str(num)

    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            return False

    return True
                              

for tc in range(1, T+1):
    N = int(input())
    A_lst = sorted(map(int, input().split()), reverse=True)

    max_product = -1
    for i in range(N):
        for j in range(i+1, N):
            product = A_lst[i] * A_lst[j]

            if product <= max_product:
                break
            if chk(product):
                max_product = product
    print(f"#{tc} {max_product}")