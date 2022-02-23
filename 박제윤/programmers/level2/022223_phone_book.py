# date: 2022.02.23
# author: jeiyoon
from typing import List

def solution(phone_book: List[str]) -> bool:
  """
  Note: it doesn't matter who is prefix of the other people 
  """
  answer = True
  """
  (1) sorted length
  """
  # phone_book의 길이는 1 이상 1,000,000 이하입니다.
  # 각 전화번호의 길이는 1 이상 20 이하입니다.
  # 같은 전화번호가 중복해서 들어있지 않습니다.
  phone_book.sort()
  
  for phone_idx in range(len(phone_book)-1):
    """
    (2) prefix?
    """
    if phone_book[phone_idx] in phone_book[phone_idx + 1][:len(phone_book[phone_idx])]:
      answer = False
  
  return answer

# return = False
# phone_book = ["119", "97674223", "1195524421"]

# return = True
# phone_book = ["123","456","789"]

# return = False
phone_book = ["12","123","1235","567","88"]

print(solution(phone_book))

"""
def solution_2(phone_book: List[str]) -> bool:
  phone_book.sort()

  # zip 이라서 하나짜리에 길이가 맞춰짐
  for p1, p2 in zip(phone_book, phone_book[1:]):
    print(p1, p2)
    # "startswith"
    if p2.startswith(p1):
        return False
  return True
"""
