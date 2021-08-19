# page: p552
# sol) XOR
from typing import List

def singleNumber(nums: List[int]) -> int:
  result = 0
  print(nums)

  for num in nums:
    print("(before) result: ", result)
    print("num: ", num)
    result ^= num
    print("result = result ^ num")
    print("(after) result: ", result)
    print(bin(result))    
    print(" ")

  return result

# result = 1
# nums = [2, 2, 1]

# result = 4
nums = [4, 1, 2, 1, 2]
# nums = [1, 1, 2, 2, 4]
# nums = [1,2,1,2]

# e.g.) if a = 6, b = 3 -> a ^ b = 5 (110 ^ 011 => 101)
print(singleNumber(nums))
