# date: 2022.01.24
# author: jeiyoon
def solution(s: str) -> str:
  result_s_str = ""
  idx = 0

  # 'enumerate" doesn't work
  for s_word in s:
    if s_word.isspace():
      result_s_str += " "
      idx = 0
      continue
    if idx % 2 == 0:
      result_s_str += s_word.upper()
    else:
      result_s_str += s_word.lower()
    idx += 1
  return result_s_str

# return = "TrY HeLlO WoRlD"
s = "try hello world"

print(solution(s))
