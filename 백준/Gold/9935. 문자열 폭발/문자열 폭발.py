arr = input()
explosion = input()

stack = []
ex_len = len(explosion)

for char in arr:
          stack.append(char)
          if char == explosion[-1] and ''.join(stack[-ex_len:]) == explosion:
                  del stack[-ex_len:]
result = ''.join(stack)

if result == '':
        print('FRULA')
else:
        print(result)
