import sys
import math
import heapq
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
          num = int(input().rstrip())

          if num != 0:
                  heapq.heappush(nums, (abs(num), num))

          else:
                  if not nums:
                          print(0)
                  else:
                          print(heapq.heappop(nums)[1])