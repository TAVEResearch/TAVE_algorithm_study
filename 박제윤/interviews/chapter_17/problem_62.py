# page: p507
# sol) sort and compare
def is_anagram(s: str, t: str) -> bool:
  return sorted(s) == sorted(t)

# true
s = "anagram"
t = "nagaram"

# false
# s = "rat"
# t = "car"

print(is_anagram(s, t))
