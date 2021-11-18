# date: 2021.11.18
# author: jeiyoon
def solution(s: str) -> str:
  if len(s) == 0:
    return ""
  return (1 - (len(s) % 2)) * s[int(len(s) / 2) - 1] + s[int(len(s) / 2)] 


# result = "c"
# s = "abcde"

# result = "we"
# s = "qwer"

print(solution(s))
