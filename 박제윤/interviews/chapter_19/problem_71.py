# page: p554
# sol) XOR

def hammingDistance(x: int, y: int) -> int:
  return bin(x ^ y).count('1')

x = 1
y = 4

print(hammingDistance(x, y))
