# page: p561
# sol) Determination based on the first byte.
from typing import List

def validUtf8(data: List[int]) -> bool:
  # by the size of character bytes, determining whether the start is "10"
  # e.g.) 3 bytes, the others should start with "10"
  def check(size):
    for i in range(start + 1, start + size + 1):
      if i >= len(data) or (data[i] >> 6) != 0b10:
        return False
    return True

  start = 0

  while start < len(data):
    # Determine the total character bytes by first byte.
    first = data[start]
    print(first)

    if (first >> 3) == 0b11110 and check(3):
      start += 4
    elif (first >> 4) == 0b1110 and check(2):
      start += 3
    elif (first >> 5) == 0b110 and check(1):
      start += 2
    elif (first >> 7) == 0:
      start += 1
    else:
      return False

  return True
    


# result = True
# data = [197, 130, 1]

# result = False
data = [235, 140, 4]

print(validUtf8(data))
