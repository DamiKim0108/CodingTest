from collections import Counter

name = list(map(str,input()))
name.sort()
count = Counter(name)
odd = 0
alpha = ''
ans = ''
for i in count:
	if count[i] % 2 != 0:
		odd += 1
		alpha += i

	for _ in range(count[i]//2):
		ans += i

if odd > 1:
	print("I'm Sorry Hansoo")

elif odd == 0:
	print(ans + ans[::-1])

else:
	print(ans + alpha + ans[::-1])