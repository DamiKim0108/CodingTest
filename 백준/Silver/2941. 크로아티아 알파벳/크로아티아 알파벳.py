dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()

for x in dic:
          str = str.replace(x, '*')

print(len(str))

