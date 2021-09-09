# date: 2021.09.09
# author: jeiyoon
def solution(price: int, money: int, count:int) -> int:
  return max(0, sum([c * price for c in range(1, count + 1)]) - money)

# result = 10
price = 3 # 3 6 9 12
money = 40	
count = 4	
