n, m = map(int, input().split())

room = [list(input()) for i in range(n)]

cnt = 0

for i in range(n):
          pre = ''
          for j in range(m):
                  if room[i][j] == '-':
                          if room[i][j] != pre:
                                  cnt += 1
                  pre = room[i][j]

for i in range(m):
        pre = ''
        for j in range(n):
                if room[j][i] == '|':
                        if room[j][i]!= pre:
                                cnt += 1
                pre = room[j][i]

print(cnt)
                              