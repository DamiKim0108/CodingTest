T = int(input())

for _ in range(T):
          N = int(input())
          
          price = list(map(int, input().split()))

          max_price = 0
          money = 0
          

          for i in range(len(price)-1, -1, -1):
                  if price[i] > max_price:
                          max_price = price[i]
                  else:
                          money += max_price - price[i]

          print(money)
                          
