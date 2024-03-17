import sys
input = sys.stdin.readline
n = int(input())

word = []
dic = {}

for _ in range(n):
          word.append(input().rstrip())


for i in word:
        cnt = len(i)
        
        for j in i:
                if j not in dic:
                        dic[j] = (10 ** (cnt-1))
                else:
                        dic[j] += (10 ** (cnt-1))
                cnt -= 1

value = list(dic.values())
value.sort(reverse=True)

num = 9
result = 0

for i in value:
        result += i * num
        num -= 1

print(result)