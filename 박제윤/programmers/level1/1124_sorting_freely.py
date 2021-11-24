# date: 2021.11.24
# author: jeiyoon
from typing import List

def solution(strings: List[str], n: int) -> List[str]:
  return sorted(strings, key=lambda str: (str[n], str))

# return =  ["car", "bed", "sun"]
# strings = ["sun", "bed", "car"]
# n = 1

# return = ["abcd", "abce", "cdx"]
strings = ["abce", "abcd", "cdx"]
n = 2

print(solution(strings, n))
