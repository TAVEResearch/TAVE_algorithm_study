# date: 2022.01.19
# author: jeiyoon
def solution(s: str) -> bool:
    try:    
      return int(s) and len(s) == 4
    except:
      return False


# return = false
s = "a234"

# return true
# s = "1234"

print(solution(s))
