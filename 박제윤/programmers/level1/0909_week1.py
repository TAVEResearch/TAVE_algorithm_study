def solution(price: int, money: int, count:int) -> int:
  return max(0, sum([c * price for c in range(1, count + 1)]) - money)
