# date: 2022.01.24
# author: jeiyoon
"""
"sorted(reverse = True)"는 원래 대문자는 소문자보다 작은 것으로 간주함
"""
def solution(s: str) -> str:
   # str은 길이 1 이상인 문자열입니다.
   if len(s) == 1:
     return s

   return "".join(sorted(s, reverse = True))


# return = "gfedcbZ"
s = "Zbcdefg"

print(solution(s))
