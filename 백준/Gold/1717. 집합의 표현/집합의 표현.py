
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
# 자기 자신을 부모로 설정

def find_parent(a):
          # 자기 자신이 부모이면 반환
          if a == parent[a]:
                  return a
          p = find_parent(parent[a])
          parent[a] = p
          return parent[a]

def union(a, b):
        a = find_parent(a)
        b = find_parent(b)

        if a==b:
                return
        if a<b:
                parent[b] = a
        else:
                parent[a] = b

for _ in range(m):
        opr, a, b = map(int, input().split())
        if opr == 0:
                union(a, b)
        else:
                if find_parent(a) == find_parent(b):
                        print("YES")
                else:
                        print("NO")
