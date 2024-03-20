n, m = map(int, input().split())
nums = []

nums = list(map(int, input().split()))

nums.sort()
tmp = 0

for i in range(m):
          nums.sort()
          tmp = 0

          tmp = nums[0] + nums[1]
          nums[0], nums[1] = tmp, tmp

print(sum(nums))