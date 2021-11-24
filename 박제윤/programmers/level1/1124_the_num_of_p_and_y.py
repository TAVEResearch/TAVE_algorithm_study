# date: 2021.11.24
# author: jeiyoon
def solution(s: str) -> bool:
  s = s.lower()
  return s.count('p') == s.count('y')

# answer = true
# s = "pPoooyY"

# answer = false
s = "Pyy"

print(solution(s))
