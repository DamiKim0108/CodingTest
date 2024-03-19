
TC = 1
while True:
          stack = []
          count = 0
          string = input()

          if '-' in string:
                  break

          for i in string:
                  if i == '{':
                          stack.append('{')
                  else:
                          if stack:
                                   stack.pop()
                          else:
                                  count += 1
                                  stack.append('{')

          count += len(stack) // 2

          print(f'{TC}. {count}')
          TC += 1