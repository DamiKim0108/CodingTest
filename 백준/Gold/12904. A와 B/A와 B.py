import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

flag = 0

while T:
          if T[-1] == 'A':
                  T.pop()

          elif T[-1] == 'B':
                  T.pop()
                  T.reverse()
          
          if S == T:
                  flag = 1
                  break

if flag == 1:
        print(1)
else:
        print(0)
 