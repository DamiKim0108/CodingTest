def dfs(idx, s_sum, k_sum):
    global max_score

    if k_sum > L:
        return
    if max_score < s_sum:
        max_score = s_sum
    if idx == N:
        return
    score, kcal = ingredients[idx]
    
    dfs(idx+1, s_sum+score, k_sum+kcal)
    dfs(idx+1, s_sum, k_sum)

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())

    ingredients = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, max_score))

