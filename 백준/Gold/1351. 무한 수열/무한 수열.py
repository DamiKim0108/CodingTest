N, P, Q = map(int, input().split())

dict = {}
dict[0] = 1

def solution(n):
          if n in dict:
                  return dict[n]
          
          else:
                  dict[n] = solution(n//P) + solution(n//Q)
                  return dict[n]
          
print(solution(N))