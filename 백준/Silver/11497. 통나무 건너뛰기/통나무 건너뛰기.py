import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
          N = int(input())
          tree = list(map(int, input().split()))
          tree.sort()
          result = abs(tree[0]-tree[1])

          for i in range(2, N):
                  result = max(result, abs(tree[i] - tree[i-2]))

          print(result)