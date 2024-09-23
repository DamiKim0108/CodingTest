# TC = 10
# 첫번째 줄에 덤프 횟수
# 다음줄에 각 상자의 높이값
# 덤프 횟수만큼 최대값과 최소값 사이 하나씩 교환

for tc in range(1, 11):
    count = int(input())
    height = list(map(int, input().split()))

    for j in range(count):
        max_height = max(height)
        min_height = min(height)

        max_idx = height.index(max_height)
        min_idx = height.index(min_height)

        height[max_idx] -= 1
        height[min_idx] += 1

    answer = max(height) - min(height)
    print('#', tc, " ", answer, sep='')



